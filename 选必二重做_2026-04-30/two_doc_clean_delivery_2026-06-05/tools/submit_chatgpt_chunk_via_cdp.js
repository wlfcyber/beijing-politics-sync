#!/usr/bin/env node
const fs = require("fs");

const [promptPath, expectedChunkId, resultPath, screenshotPath] = process.argv.slice(2);
if (!promptPath || !expectedChunkId || !resultPath || !screenshotPath) {
  console.error("usage: submit_chatgpt_chunk_via_cdp.js PROMPT EXPECTED_CHUNK_ID RESULT_MD SCREENSHOT_PNG");
  process.exit(2);
}

async function cdpFor(target) {
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  let seq = 0;
  const pending = new Map();

  function send(method, params = {}, timeoutMs = 30000) {
    const id = ++seq;
    ws.send(JSON.stringify({ id, method, params }));
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        pending.delete(id);
        reject(new Error(`CDP timeout: ${method}`));
      }, timeoutMs);
      pending.set(id, {
        method,
        resolve: (v) => {
          clearTimeout(timer);
          resolve(v);
        },
        reject,
      });
    });
  }

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) p.reject(new Error(`${p.method}: ${msg.error.message}`));
      else p.resolve(msg.result);
    }
  };

  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });
  return { ws, send };
}

async function main() {
  const prompt = fs.readFileSync(promptPath, "utf8");
  const target = await (await fetch("http://127.0.0.1:9222/json/new?https://chatgpt.com/", { method: "PUT" })).json();
  console.log("target", target.id, target.url);
  const { ws, send } = await cdpFor(target);
  await send("Runtime.enable");
  await send("Page.enable");
  await fetch(`http://127.0.0.1:9222/json/activate/${target.id}`);

  await new Promise((resolve) => setTimeout(resolve, 5000));

  const focusExpr = `(() => {
    const el = document.querySelector('#prompt-textarea') || document.querySelector('div[contenteditable="true"]') || document.querySelector('textarea');
    if (!el) return {ok:false, reason:'no input', body: document.body.innerText.slice(0,800)};
    el.focus();
    if (el.tagName === 'TEXTAREA') { el.value = ''; el.dispatchEvent(new Event('input', {bubbles:true})); }
    else { el.innerHTML = ''; el.dispatchEvent(new InputEvent('input', {bubbles:true, inputType:'deleteContentBackward'})); }
    return {ok:true, tag:el.tagName, id:el.id};
  })()`;
  const focus = await send("Runtime.evaluate", { expression: focusExpr, returnByValue: true });
  if (!focus.result.value?.ok) throw new Error(`input not found: ${JSON.stringify(focus.result.value)}`);
  console.log("focus", JSON.stringify(focus.result.value));

  async function clearInput() {
    await send("Runtime.evaluate", { expression: focusExpr, returnByValue: true }, 60000);
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }

  async function readInputState() {
    return await send("Runtime.evaluate", {
    expression: `(() => {
      const el = document.querySelector('#prompt-textarea') || document.querySelector('div[contenteditable="true"]') || document.querySelector('textarea');
      if (!el) return {ok:false, reason:'no input after insert'};
      const text = el.tagName === 'TEXTAREA' ? el.value : el.innerText;
      const beginInstructions = text.indexOf('BEGIN_REVIEW_INSTRUCTIONS');
      const endInstructions = text.indexOf('END_REVIEW_INSTRUCTIONS');
      const beginContent = text.indexOf('BEGIN_CHUNK_CONTENT');
      const endContent = text.indexOf('END_CHUNK_CONTENT');
      const hasSentinels = beginInstructions >= 0 || endInstructions >= 0 || beginContent >= 0 || endContent >= 0;
      const endToken = 'END_CHUNK_CONTENT';
      const extraAfterEnd = endContent >= 0 ? text.slice(endContent + endToken.length).trim() : '';
      const sentinelOrderOk = !hasSentinels || (
        beginInstructions >= 0 &&
        endInstructions > beginInstructions &&
        beginContent > endInstructions &&
        endContent > beginContent &&
        extraAfterEnd.length === 0
      );
      return {
        ok: text.length > ${Math.min(prompt.length, 1000)} && text.includes(${JSON.stringify(expectedChunkId)}) && sentinelOrderOk,
        length: text.length,
        expectedLength: ${prompt.length},
        hasChunk: text.includes(${JSON.stringify(expectedChunkId)}),
        hasSentinels,
        sentinelOrderOk,
        extraAfterEndLength: extraAfterEnd.length,
        sentinelIndexes: {beginInstructions, endInstructions, beginContent, endContent},
        head: text.slice(0, 80),
        tail: text.slice(-120)
      };
    })()`,
    returnByValue: true,
    }, 60000);
  }

  async function insertPrompt({chunkSize, delayMs}) {
    for (let i = 0; i < prompt.length; i += chunkSize) {
      await send("Input.insertText", { text: prompt.slice(i, i + chunkSize) }, 120000);
      await new Promise((resolve) => setTimeout(resolve, delayMs));
    }
    await new Promise((resolve) => setTimeout(resolve, 2200));
    return await readInputState();
  }

  let inputState = await insertPrompt({chunkSize: prompt.length, delayMs: 0});
  if (!inputState.result.value?.ok) {
    console.log("inputStateRetryNeeded", JSON.stringify(inputState.result.value));
    await clearInput();
    inputState = await insertPrompt({chunkSize: 1200, delayMs: 320});
  }
  console.log("inputState", JSON.stringify(inputState.result.value));
  if (!inputState.result.value?.ok) {
    throw new Error(`prompt insertion incomplete: ${JSON.stringify(inputState.result.value)}`);
  }

  const clickExpr = `(() => {
    const candidates = [...document.querySelectorAll('button')];
    const btn = candidates.find(b => ['send-button','composer-submit-button'].includes(b.getAttribute('data-testid'))) ||
      candidates.find(b => /发送|Send/i.test(b.getAttribute('aria-label') || '')) ||
      [...candidates].reverse().find(b => !b.disabled && (b.querySelector('svg') || b.innerText.trim()===''));
    if (!btn) return {ok:false, reason:'no send button', buttons:candidates.slice(-10).map(b=>({aria:b.getAttribute('aria-label'), testid:b.getAttribute('data-testid'), disabled:b.disabled, text:b.innerText}))};
    btn.click();
    return {ok:true, aria:btn.getAttribute('aria-label'), testid:btn.getAttribute('data-testid')};
  })()`;
  const clicked = await send("Runtime.evaluate", { expression: clickExpr, returnByValue: true });
  if (!clicked.result.value?.ok) throw new Error(`send button failed: ${JSON.stringify(clicked.result.value)}`);
  console.log("clicked", JSON.stringify(clicked.result.value));

  let body = "";
  let lastAssistant = "";
  let stableHits = 0;
  const started = Date.now();
  while (Date.now() - started < 8 * 60 * 1000) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const state = await send("Runtime.evaluate", {
      expression: `(() => {
        const body = document.body.innerText;
        const assistantNodes = [
          ...document.querySelectorAll('[data-message-author-role="assistant"]'),
          ...[...document.querySelectorAll('section[data-testid^="conversation-turn-"]')]
            .filter(n => !n.querySelector('[data-message-author-role="user"]')),
          ...document.querySelectorAll('main div.markdown')
        ];
        const assistants = assistantNodes
          .map(n => n.innerText.trim())
          .filter(t => t && !t.startsWith('# External Review Context'));
        const lastAssistant = assistants[assistants.length - 1] || '';
        const generating = [...document.querySelectorAll('button')].some(b => /停止|Stop/i.test((b.getAttribute('aria-label') || '') + ' ' + b.innerText));
        return {body, lastAssistant, generating};
      })()`,
      returnByValue: true,
    }, 60000);
    body = state.result.value.body || "";
    lastAssistant = state.result.value.lastAssistant || "";
    const inspectText = lastAssistant || body;
    const hasChunk = inspectText.includes(expectedChunkId);
    const hasVerdict = /["“”]?verdict["“”]?\s*[:：]\s*["“”]?(PASS|CONDITIONAL_PASS|FAIL)["“”]?/i.test(inspectText);
    console.log("poll", Math.round((Date.now() - started) / 1000), { hasChunk, hasVerdict, generating: state.result.value.generating, bodyLen: body.length, assistantLen: lastAssistant.length });
    if (hasChunk && hasVerdict && !state.result.value.generating) {
      stableHits += 1;
      if (stableHits >= 2) break;
    } else {
      stableHits = 0;
    }
  }

  const screenshot = await send("Page.captureScreenshot", { format: "png", fromSurface: true }, 60000);
  fs.writeFileSync(screenshotPath, Buffer.from(screenshot.data, "base64"));

  const sourceText = lastAssistant || body;
  const idx = Math.max(sourceText.lastIndexOf(`chunk_id: ${expectedChunkId}`), sourceText.lastIndexOf(`chunk_id：${expectedChunkId}`), sourceText.lastIndexOf(expectedChunkId));
  const extracted = idx >= 0 ? sourceText.slice(idx, idx + 5000) : sourceText.slice(-5000);
  const markdown = `# GPT-5.5 Pro Web Result - ${expectedChunkId}

- reviewed_via: Chrome visible ChatGPT web session through CDP browser automation
- model_surface_seen: Pro / 进阶专业
- submitted_at: ${new Date().toISOString()}
- prompt: \`${promptPath}\`
- screenshot: \`${screenshotPath}\`

## Extracted Result Tail

\`\`\`text
${extracted.trim()}
\`\`\`
`;
  fs.writeFileSync(resultPath, markdown, "utf8");
  console.log(resultPath);
  console.log(screenshotPath);
  ws.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

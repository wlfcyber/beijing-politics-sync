import argparse
import json
import time
import urllib.request
from itertools import count
from pathlib import Path

import websocket


def get_chatgpt_page(port: int):
    pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list"))
    for page in pages:
        if "chatgpt.com" in page.get("url", "") and page.get("type") == "page":
            return page
    raise RuntimeError("No ChatGPT page found on the requested CDP port")


class CDP:
    def __init__(self, ws_url: str):
        self.ws = websocket.create_connection(ws_url, timeout=15, suppress_origin=True)
        self.ids = count(1)

    def call(self, method: str, params=None, timeout=60):
        msg_id = next(self.ids)
        self.ws.settimeout(timeout)
        self.ws.send(json.dumps({"id": msg_id, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == msg_id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def evaluate(self, expression: str, timeout=60, return_by_value=True):
        return self.call(
            "Runtime.evaluate",
            {
                "expression": expression,
                "awaitPromise": True,
                "returnByValue": return_by_value,
            },
            timeout=timeout,
        )

    def close(self):
        self.ws.close()


def js_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--wait-seconds", type=int, default=900)
    ap.add_argument("--new-chat", action="store_true")
    ap.add_argument("--capture-only", action="store_true")
    args = ap.parse_args()

    prompt = Path(args.prompt).read_text(encoding="utf-8")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    page = get_chatgpt_page(args.port)
    cdp = CDP(page["webSocketDebuggerUrl"])
    try:
        cdp.call("Runtime.enable")
        if args.new_chat:
            cdp.call("Page.navigate", {"url": "https://chatgpt.com/"})
            time.sleep(5)

        if not args.capture_only:
            focus_expr = """
        (() => {
          const el = document.querySelector('div.ProseMirror[contenteditable="true"], div.ProseMirror[role="textbox"], textarea[aria-label*="ChatGPT"], textarea[aria-label*="聊天"]');
          if (!el) return {ok:false, reason:'no composer'};
          el.focus();
          return {ok:true, tag:el.tagName, role:el.getAttribute('role'), aria:el.getAttribute('aria-label')};
        })()
        """
            focus_res = cdp.evaluate(focus_expr)["result"].get("value")
            if not focus_res or not focus_res.get("ok"):
                raise RuntimeError(f"Could not focus composer: {focus_res}")

            cdp.call("Input.insertText", {"text": prompt}, timeout=120)
            time.sleep(2)

            send_expr = """
        (() => {
          const candidates = [
            'button[data-testid="send-button"]',
            'button[aria-label*="发送"]',
            'button[aria-label*="Send"]'
          ];
          for (const sel of candidates) {
            const btn = document.querySelector(sel);
            if (btn && !btn.disabled) {
              btn.click();
              return {ok:true, selector:sel};
            }
          }
          const buttons = [...document.querySelectorAll('button')];
          const visible = buttons.map((b, i) => ({i, aria:b.getAttribute('aria-label'), text:b.innerText, disabled:b.disabled})).slice(-30);
          return {ok:false, buttons:visible};
        })()
        """
            send_res = cdp.evaluate(send_expr)["result"].get("value")
            if not send_res or not send_res.get("ok"):
                raise RuntimeError(f"Could not click send: {send_res}")
        else:
            send_res = {"ok": True, "selector": "capture-only"}

        start = time.time()
        last_text = ""
        stable_since = time.time()
        capture = {}
        while time.time() - start < args.wait_seconds:
            capture_expr = """
            (() => {
              const assistantNodes = [...document.querySelectorAll('[data-message-author-role="assistant"], article')];
              const texts = assistantNodes.map(n => n.innerText || '').filter(Boolean);
              const body = document.body.innerText || '';
              const busy = /停止生成|Stop generating|正在生成|Thinking|思考中|Pro 思考中|正在思考/.test(body);
              const last = texts.length ? texts[texts.length - 1] : body.slice(-4000);
              return {url:location.href, title:document.title, busy, count:texts.length, last, bodyTail:body.slice(-4000)};
            })()
            """
            capture = cdp.evaluate(capture_expr, timeout=30)["result"].get("value") or {}
            current = capture.get("last", "")
            if current != last_text:
                last_text = current
                stable_since = time.time()
            if len(current.strip()) > 200 and not capture.get("busy") and time.time() - stable_since > 25:
                break
            time.sleep(5)

        saved = {
            "captured_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "page": page,
            "send": send_res,
            "capture": capture,
        }
        out.write_text(
            f"# GPT Pro Web Capture\n\n"
            f"- captured_at: {saved['captured_at']}\n"
            f"- url: {capture.get('url','')}\n"
            f"- assistant_blocks_seen: {capture.get('count','')}\n\n"
            f"## Last Assistant Output\n\n{capture.get('last','')}\n",
            encoding="utf-8",
        )
        print(json.dumps({"ok": True, "output": str(out), "chars": len(capture.get("last", "")), "url": capture.get("url", "")}, ensure_ascii=False))
    finally:
        cdp.close()


if __name__ == "__main__":
    main()

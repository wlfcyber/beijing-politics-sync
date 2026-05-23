import argparse
import json
import time
import urllib.request
from itertools import count
from pathlib import Path

import websocket


def page_for(port: int):
    pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list"))
    for page in pages:
        if "chatgpt.com" in page.get("url", "") and page.get("type") == "page":
            return page
    raise RuntimeError("No ChatGPT page found")


class CDP:
    def __init__(self, ws_url: str):
        self.ws = websocket.create_connection(ws_url, timeout=20, suppress_origin=True)
        self.ids = count(1)

    def call(self, method: str, params=None, timeout=90):
        msg_id = next(self.ids)
        self.ws.settimeout(timeout)
        self.ws.send(json.dumps({"id": msg_id, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == msg_id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def eval(self, expression: str, timeout=90):
        return self.call("Runtime.evaluate", {"expression": expression, "awaitPromise": True, "returnByValue": True}, timeout=timeout)

    def close(self):
        self.ws.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", nargs="+", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--wait-seconds", type=int, default=1800)
    ap.add_argument("--new-chat", action="store_true")
    args = ap.parse_args()

    files = [str(Path(p).resolve()) for p in args.files]
    for f in files:
        if not Path(f).exists():
            raise FileNotFoundError(f)
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    page = page_for(args.port)
    cdp = CDP(page["webSocketDebuggerUrl"])
    try:
        cdp.call("Runtime.enable")
        cdp.call("DOM.enable")
        if args.new_chat:
            cdp.call("Page.navigate", {"url": "https://chatgpt.com/"})
            time.sleep(6)

        doc = cdp.call("DOM.getDocument", {"depth": 1})
        root = doc["root"]["nodeId"]
        node = cdp.call("DOM.querySelector", {"nodeId": root, "selector": "input[type=file]:not([accept='image/*'])"})
        node_id = node.get("nodeId")
        if not node_id:
            node = cdp.call("DOM.querySelector", {"nodeId": root, "selector": "input[type=file]"})
            node_id = node.get("nodeId")
        if not node_id:
            raise RuntimeError("No file input found")
        cdp.call("DOM.setFileInputFiles", {"nodeId": node_id, "files": files}, timeout=120)

        # Wait for upload chips or file names to appear and settle.
        names = [Path(f).name for f in files]
        start_upload = time.time()
        while time.time() - start_upload < 180:
            status = cdp.eval(
                """
                (() => {
                  const body = document.body.innerText || '';
                  const busy = /上传|Uploading|处理|Processing|读取|Reading/.test(body);
                  return {body, busy};
                })()
                """,
                timeout=30,
            )["result"]["value"]
            body = status.get("body", "")
            if all(name in body for name in names) and not status.get("busy"):
                break
            time.sleep(3)

        cdp.eval(
            """
            (() => {
              const el = document.querySelector('div.ProseMirror[contenteditable="true"], div.ProseMirror[role="textbox"], textarea[aria-label*="ChatGPT"], textarea[aria-label*="聊天"]');
              if (!el) return false;
              el.focus();
              return true;
            })()
            """,
            timeout=30,
        )
        cdp.call("Input.insertText", {"text": prompt}, timeout=60)
        time.sleep(2)
        send = cdp.eval(
            """
            (() => {
              const sels = ['button[data-testid="send-button"]', 'button[aria-label*="发送"]', 'button[aria-label*="Send"]'];
              for (const sel of sels) {
                const btn = document.querySelector(sel);
                if (btn && !btn.disabled) { btn.click(); return {ok:true, sel}; }
              }
              return {ok:false, buttons:[...document.querySelectorAll('button')].slice(-20).map(b=>({aria:b.getAttribute('aria-label'), text:b.innerText, disabled:b.disabled, testid:b.getAttribute('data-testid')}))};
            })()
            """,
            timeout=30,
        )["result"]["value"]
        if not send.get("ok"):
            raise RuntimeError(f"Could not send: {send}")

        last_text = ""
        stable_since = time.time()
        capture = {}
        start = time.time()
        while time.time() - start < args.wait_seconds:
            capture = cdp.eval(
                """
                (() => {
                  const body = document.body.innerText || '';
                  const nodes = [...document.querySelectorAll('[data-message-author-role="assistant"], div.markdown')];
                  const texts = nodes.map(n => n.innerText || '').filter(Boolean);
                  const busy = /停止回答|停止生成|Stop generating|思考中|Pro 思考中|正在思考|Thinking/.test(body);
                  return {url:location.href, busy, count:texts.length, last:texts.length ? texts[texts.length-1] : '', bodyTail:body.slice(-3000)};
                })()
                """,
                timeout=30,
            )["result"]["value"]
            cur = capture.get("last", "")
            if cur != last_text:
                last_text = cur
                stable_since = time.time()
            if len(cur.strip()) > 200 and not capture.get("busy") and time.time() - stable_since > 25:
                break
            time.sleep(5)

        out.write_text(
            "# GPT Pro File Upload Capture\n\n"
            + f"- url: {capture.get('url','')}\n"
            + f"- files: {', '.join(Path(f).name for f in files)}\n"
            + f"- chars: {len(capture.get('last',''))}\n\n"
            + "## Last Assistant Output\n\n"
            + capture.get("last", ""),
            encoding="utf-8",
        )
        print(json.dumps({"ok": True, "chars": len(capture.get("last", "")), "output": str(out), "url": capture.get("url", "")}, ensure_ascii=False))
    finally:
        cdp.close()


if __name__ == "__main__":
    main()

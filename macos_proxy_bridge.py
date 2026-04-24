#!/usr/bin/env python3
import base64
import os
import select
import socket
import socketserver
import sys


LISTEN_HOST = os.environ.get("LISTEN_HOST", "127.0.0.1")
LISTEN_PORT = int(os.environ.get("LISTEN_PORT", "18001"))
UPSTREAM_HOST = os.environ["UPSTREAM_HOST"]
UPSTREAM_PORT = int(os.environ["UPSTREAM_PORT"])
UPSTREAM_USERNAME = os.environ["UPSTREAM_USERNAME"]
UPSTREAM_PASSWORD = os.environ["UPSTREAM_PASSWORD"]

AUTH_VALUE = "Basic " + base64.b64encode(
    f"{UPSTREAM_USERNAME}:{UPSTREAM_PASSWORD}".encode("utf-8")
).decode("ascii")


class ProxyHandler(socketserver.BaseRequestHandler):
    timeout = 60

    def handle(self):
        client = self.request
        client.settimeout(self.timeout)
        try:
            header = self._read_header(client)
            if not header:
                return

            upstream = socket.create_connection(
                (UPSTREAM_HOST, UPSTREAM_PORT),
                timeout=self.timeout,
            )
            upstream.settimeout(self.timeout)
            try:
                upstream.sendall(self._with_proxy_auth(header))
                self._relay(client, upstream)
            finally:
                upstream.close()
        except Exception as exc:
            sys.stderr.write(f"bridge error: {exc}\n")
            sys.stderr.flush()

    def _read_header(self, sock):
        data = b""
        while b"\r\n\r\n" not in data and len(data) < 65536:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
        return data

    def _with_proxy_auth(self, header):
        marker = b"\r\n\r\n"
        if marker not in header:
            return header

        head, rest = header.split(marker, 1)
        lines = head.split(b"\r\n")
        filtered = [
            line for line in lines
            if not line.lower().startswith(b"proxy-authorization:")
        ]
        filtered.append(f"Proxy-Authorization: {AUTH_VALUE}".encode("ascii"))
        return b"\r\n".join(filtered) + marker + rest

    def _relay(self, left, right):
        sockets = [left, right]
        while True:
            readable, _, errored = select.select(sockets, [], sockets, self.timeout)
            if errored or not readable:
                return

            for sock in readable:
                other = right if sock is left else left
                data = sock.recv(65536)
                if not data:
                    return
                other.sendall(data)


class ThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    with ThreadingTCPServer((LISTEN_HOST, LISTEN_PORT), ProxyHandler) as server:
        print(f"California proxy bridge listening on {LISTEN_HOST}:{LISTEN_PORT}", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()

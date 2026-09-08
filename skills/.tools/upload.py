#!/usr/bin/env python3
"""Upload a file to the OSS gateway for cross-agent sharing.

Usage: python .tools/upload.py <file_path> [object_key]
Returns the public URL on stdout (single line).
"""
import json
import sys
import urllib.request
import uuid

GATEWAY = "https://discovery-staging.intern-ai.org.cn/transfer/api/v1/files"
MAX_SIZE = 100 * 1024 * 1024  # 100 MB


def upload(path: str, object_key: str | None = None) -> str:
    with open(path, "rb") as f:
        data = f.read()
    if not data:
        print("ERROR: empty file", file=sys.stderr)
        sys.exit(1)
    if len(data) > MAX_SIZE:
        print(f"ERROR: file exceeds 100 MB ({len(data)} bytes)", file=sys.stderr)
        sys.exit(1)

    boundary = uuid.uuid4().hex
    filename = path.replace("\\", "/").rsplit("/", 1)[-1]

    parts = []
    parts.append(
        (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
            f"Content-Type: application/octet-stream\r\n\r\n"
        ).encode()
        + data
    )
    if object_key:
        parts.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="object_key"\r\n\r\n'
                f"{object_key}\r\n"
            ).encode()
        )
    parts.append(f"\r\n--{boundary}--\r\n".encode())
    body = b"".join(parts)

    req = urllib.request.Request(
        GATEWAY,
        data=body,
        method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    resp = urllib.request.urlopen(req, timeout=300)
    result = json.loads(resp.read())
    return result["url"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file> [object_key]", file=sys.stderr)
        sys.exit(1)
    url = upload(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(url)

---
name: molclaw-file-transfer
description: Implement data transmission between the local computer and the MCP server using Base64 encoding
license: MIT license
metadata:
    skill-author: PJLab
---

# File Transfer

Note:
- Local files are not directly accessible by the server. Upload them to the server using this skill before execution.
- For PDB file inputs, it is recommended to preprocess them using `molclaw-pdbfixer` before execution.
- Tools are native MCP tools (`mcp__DrugSDA-Tool__*`), already available in the tool list.

### 1. Transfer local file to SCP server

Tools: `mcp__DrugSDA-Tool__base64_to_server_file`

1. Encode the local file with Bash: `base64 -w0 /path/a.txt` (single-line base64 string).
2. Call `mcp__DrugSDA-Tool__base64_to_server_file` with:

```json
{
    "file_name": "a.txt",
    "file_base64_string": "<base64 output of the local file>"
}
```

3. The result contains `save_file` — the server file path to use in subsequent tools.

### 2. Transfer SCP server file to local

Tools: `mcp__DrugSDA-Tool__server_file_to_base64`

1. Call `mcp__DrugSDA-Tool__server_file_to_base64` with:

```json
{
    "file_path": "/path/a.txt"
}
```

2. The result contains `base64_string` and `file_name`.
3. Decode to a local file with Bash: write `base64_string` to a temporary file (or pass it inline for short content) and run `base64 -d tmp.b64 > /path/a.txt`.

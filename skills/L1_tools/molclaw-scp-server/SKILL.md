---
name: molclaw-scp-server
description: All tools utilized within MolClaw skills are provided by the host environment as native MCP tools (mcp__DrugSDA-Tool__*). This skill describes the toolset and the calling convention used across the skill docs.
license: MIT license
metadata:
    skill-author: PJLab
---

SCP (Science Context Protocol) is an open-source standard protocol designed to accelerate scientific discovery by building a global collaboration network for autonomous scientific agents, connecting heterogeneous scientific resources (software tools, AI models, datasets, workflow engines, lab instruments, etc.).

### 1. Tool availability

All MolClaw computation tools — docking, molecular sampling, ADMET, protein structure retrieval, MD, visualization, file transfer — are served by a single MCP deployment (**DrugSDA-Tool**, 81 tools). The host environment establishes the connection before the session starts, so every tool is already present in the tool list under the `mcp__DrugSDA-Tool__` namespace, for example:

- `mcp__DrugSDA-Tool__molecule_docking_quickvina_fullprocess`
- `mcp__DrugSDA-Tool__retrieve_protein_structure_by_pdb_id`
- `mcp__DrugSDA-Tool__pred_mol_admet`

Invoke them like any other tool, with the arguments documented in each skill. Credentials (`SCP_HUB_API_KEY`) and endpoint management belong to the host environment, never to a task.

### 2. Reading the reference blocks in other skills

Each skill documents its tool's input arguments and output fields in a reference block (mirroring the server's own tool description). Invoke the tool itself with those arguments; the reference block is documentation, not code to reproduce.

### 3. Self-hosted deployments

Outside a managed host, provision the MCP server yourself and register it in your agent runtime's MCP configuration: streamable HTTP endpoint `https://scp.intern-ai.org.cn/api/v1/mcp/2/DrugSDA-Tool`, auth header `SCP-HUB-API-KEY`, key from the repository `.env.template` (apply at <https://github.com/InternScience/scp>). See the repository README for details.

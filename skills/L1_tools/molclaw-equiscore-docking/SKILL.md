---
name: molclaw-equiscore-docking
description: End-to-end docking-score ranking using EquiScore for candidate molecules against a target protein.
license: MIT license
metadata:
    skill-author: PJLab
---

# 1. EquiScore Docking Ranking Skill

Note: 
- Local files are not directly accessible by the server. Please upload them to the server using `molclaw-file-transfer` before execution. 
- For PDB file inputs, it is recommended to preprocess them using `molclaw-pdbfixer` before execution.
- Please refer to skill `molclaw-scp-server` to complete tool invocation.

step 1. Retrieve target protein structure (skip if user already provides PDB).
- Use skill `molclaw-protein-structure-retrieve`.

step 2. Optional chain extraction (only if specific chains are required).

Invoke `mcp__DrugSDA-Tool__extract_and_save_chains` with the arguments documented above; use the result fields `out_file`.

step 3. Fix receptor structure with PDBFixer.

Invoke `mcp__DrugSDA-Tool__fix_pdb` with the arguments documented above; use the result fields `output_file`.

## 2. EquiScore-based Ranking Flow

step 4. Drug-likeness filtering.
- Keep molecules satisfying: `QED >= 0.2` and `lipinski_rule_of_5_violations <= 2`.
- Always compute from returned `result["metrics"]`; do not use manually copied values.
- Assert `len(metrics) == len(candidate_smiles_list)` before filtering.

Invoke `mcp__DrugSDA-Tool__calculate_mol_drug_chemistry` with the arguments documented above; use the result fields `metrics`, `smiles`, `qed`, `lipinski_rule_of_5_violations`.

step 5. Build EquiScore docking input.

Important:
- EquiScore needs a docking-result SDF (ligand poses relative to receptor).
- Raw SDF converted directly from SMILES is not sufficient for `equiscore_pocket`.

Two valid modes:
- Mode A: user already provides `docking_result_sdf_path` -> use directly.

- Mode B: only SMILES provided -> first generate docking poses using `molecule_docking_quickvina_fullprocess`, then perform a **pose-preserving** PDBQT-to-SDF conversion and set `docking_result_sdf_path` to that converted docked file before continuing to step 6.

The deployed `convert_smiles_to_format` tool accepts SMILES strings or `.smi` files; it does **not** convert an existing docked PDBQT pose. Using it here would regenerate ligand coordinates and lose the receptor-relative pose. Perform the file conversion with a pose-preserving converter such as Open Babel where available, then upload the resulting SDF with `molclaw-file-transfer`. If no such conversion path is available, require an already docked SDF instead of substituting a raw SMILES-derived SDF.

step 6. Run EquiScore pocket extraction first.
- Use `molclaw-equiscore-tool` -> `equiscore_pocket`.
- Before first call, verify tool argument names from schema (`list_tools` + `inputSchema`) if uncertain.

Invoke `mcp__DrugSDA-Tool__equiscore_pocket` with the arguments documented above; use the result fields `pocket_dir`.

If `split_sdf_count == 0` or `pocket_item_count == 0`, fix docking input first and rerun this step.

step 7. Run EquiScore screening.
- Use `molclaw-equiscore-tool` -> `equiscore_screen`.

Invoke `mcp__DrugSDA-Tool__equiscore_screen` with the arguments documented above; use the result fields `predictions_path`, `score_field`.

step 8. Rank and return.
- Prefer direct CSV read from `predictions_path`.
- If direct read fails, use `molclaw-file-transfer` (`server_file_to_base64`) to fetch CSV and parse locally.
- Preserve `ligand_to_smiles_map`; do not assume CSV always has a `smiles` column.

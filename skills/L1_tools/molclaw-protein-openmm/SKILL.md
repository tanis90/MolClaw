---
name: molclaw-protein-openmm
description: Run OpenMM protein MD and extract evenly spaced trajectory frames for downstream structural analysis.
license: MIT license
metadata:
    skill-author: PJLab
---

# Protein OpenMM MD and Frame Extraction

Note: 
- Local files are not directly accessible by the server. Please upload them to the server using `molclaw-file-transfer` before execution. 
- For PDB file inputs, it is recommended to preprocess them using `molclaw-pdbfixer` before execution.
- Please refer to skill `molclaw-scp-server` to complete tool invocation.

## Usage

### 1. Protein OpenMM MD
The description of tool *protein_openmm_md*.

```tex
Runs OpenMM-based protein molecular dynamics preparation and simulation for structure refinement workflows.
Args:
    protein_pdb (str): Absolute or relative path to input protein PDB.
    solvent_type (str): Solvent mode, 'explicit' or 'implicit', default 'explicit'.
    gb_model (str): GB model for implicit solvent mode, default 'GBn2'.
    water_model (str): Water model for explicit solvent mode, default 'tip3p'.
    force_field (str): OpenMM force field name, default 'amber14'.
    md_time (float): Production MD time in picoseconds, default 100000.0.
    platform (str): OpenMM compute platform, default 'CUDA'.
    full_md (bool): Run full MD procedure if True, default False.
Return:
    status (str): 'success' or 'error'.
    msg (str): Human-readable execution summary.
    command (str): The invoked command ('protein_openmm_md').
    run_dir (str | None): Final run directory under tool_result/openmm_md_result.
    work_dir (str | None): Same as run_dir for compatibility.
    trajectory_path (str | None): Path to md_traj.dcd when available.
    energy_log (str | None): Path to md.log when available.
    generated_files (List[str]): File paths relative to work_dir.
    md_time (float): Echoed requested MD time in ps.
    solvent_type (str): Echoed solvent mode.
    force_field (str): Echoed force field.
    full_md (bool): Echoed full MD mode.
```

How to use tool *protein_openmm_md* :

Invoke `mcp__DrugSDA-Tool__protein_openmm_md` with the arguments documented above; use the result fields `work_dir`.

#### Example parameter sets

```python
# 1) Main mode
{
    "protein_pdb": "/path/to/input.pdb",
    "solvent_type": "implicit",
    "gb_model": "OBC2",
    "water_model": "tip3p",
    "force_field": "amber14",
    "md_time": 1000.0,
    "platform": "CUDA",
    "full_md": True
}

# 2) Variant mode
{
    "protein_pdb": "relative/path/to/protein.pdb",
    "solvent_type": "explicit",
    "water_model": "tip3p",
    "force_field": "charmm36",
    "md_time": 10000.0,
    "platform": "CUDA",
    "full_md": False
}
```

### 2. OpenMM Trajectory Frame Extraction
The description of tool *openmm_extract_frames*.

```tex
Extracts evenly spaced protein conformations from an OpenMM work directory for downstream screening and ensemble analysis.
Args:
    work_dir (str): OpenMM MD output directory containing topology and trajectory files.
    num_frames (int): Number of evenly spaced frames to extract, default 100.
    protein_only (bool): Keep only protein atoms in extracted frames, default False.
    align (bool): Align extracted structures to the first frame, default False.
    prefix (str): Filename prefix for extracted PDB frames, default 'frame'.
    dry_run (bool): Validate inputs and prepare output directory without extraction, default False.
Return:
    status (str): 'success', 'partial_success', or 'error'.
    msg (str): Human-readable extraction summary.
    output_dir (str): Run-specific directory under tool_result/openmm_md_result.
    work_dir (str): Resolved OpenMM working directory.
    topology_path (str | None): Resolved topology file path.
    trajectory_path (str | None): Resolved trajectory file path.
    frames_dir (str): Directory where extracted frame PDB files are saved.
    frame_count (int): Number of extracted frame files.
    frame_files (List[str]): Extracted frame file paths relative to output_dir.
```

How to use tool *openmm_extract_frames* :

Invoke `mcp__DrugSDA-Tool__openmm_extract_frames` with the arguments documented above; use the result fields `frame_files`.

#### Example parameter sets

```python
# 1) Main mode
{
    "work_dir": "/path/to/work_dir",
    "num_frames": 100,
    "protein_only": False,
    "align": False,
    "prefix": "frame",
    "dry_run": False
}

# 2) Variant mode
{
    "work_dir": "relative/path/to/openmm_md_output",
    "num_frames": 50,
    "protein_only": True,
    "align": True,
    "prefix": "conf",
    "dry_run": False
}
```

### 3. End-to-End Collaboration Workflow
Use the two tools in sequence via API calls:
1. Call *protein_openmm_md* to generate MD outputs and get `work_dir`.
2. Pass that `work_dir` into *openmm_extract_frames* to extract evenly spaced PDB frames.

Invoke `mcp__DrugSDA-Tool__protein_openmm_md` and then `mcp__DrugSDA-Tool__openmm_extract_frames` with the arguments documented above; use the result fields `work_dir`, `frame_files`.

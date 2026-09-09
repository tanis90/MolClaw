---
name: molclaw-p2rank
description: Use P2Rank to locate binding pockets in the input protein. Unless specified by the user, prioritize using fpocket. 
license: MIT license
metadata:
    skill-author: PJLab
---

# Pocket Location

Note: 
- Local files are not directly accessible by the server. Please upload them to the server using `molclaw-file-transfer` before execution. 
- For PDB file inputs, it is recommended to preprocess them using `molclaw-pdbfixer` before execution.
- Please refer to skill `molclaw-scp-server` to complete tool invocation.

The description of tool *pred_pocket_prank*.

```tex
Use P2Rank to predict ligand binding pockets in the input protein.
Args:
    pdb_file_path (str): Path to the protein structure file (PDB format)
Return:
    status (str): success/error
    msg (str): message
    pred_pockets (List[dict]): List of dict, each containing pocket confidence and center position information. The first pocket (pred_pockets[0]) has the highest score and is usually used for molecular docking.
        --site_id (str): Pocket id
        --probability (float): Predicted confidence score (0~1) of the pocket
        --center_x (float): Center X of the pocket
        --center_y (float): Center Y of the pocket 
        --center_z (float): Center Z of the pocket
```

How to use tool *pred_pocket_prank* :

Invoke `mcp__DrugSDA-Tool__pred_pocket_prank` with the arguments documented above; use the result fields `pred_pockets`.

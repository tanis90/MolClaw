---
name: molclaw-esmfold
description: Use ESMFold model to predict 3D structure of the input protein sequence. 
license: MIT license
metadata:
    skill-author: PJLab
---

# Protein Structure Prediction

Note: 
- Local files are not directly accessible by the server. Please upload them to the server using `molclaw-file-transfer` before execution. 
- For PDB file inputs, it is recommended to preprocess them using `molclaw-pdbfixer` before execution.
- Please refer to skill `molclaw-scp-server` to complete tool invocation.

The description of tool *pred_protein_structure_esmfold*.

```tex
Use the ESMFold model for protein 3D structure prediction.
Args:
    sequence (str): Protein sequence
Return:
    status: success/error
    msg: message
    pdb_path (str): The predicted pdb file path
```

How to use tool *pred_protein_structure_esmfold* :

Invoke `mcp__DrugSDA-Tool__pred_protein_structure_esmfold` with the arguments documented above; use the result fields `pdb_path`.

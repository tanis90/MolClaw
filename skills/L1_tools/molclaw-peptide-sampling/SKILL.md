---
name: molclaw-peptide-sampling
description: Generate new peptide molecules sampling from the input peptide sequence. 
license: MIT license
metadata:
    skill-author: PJLab
---

# Peptide Molecule Generation

Note: 
- Local files are not directly accessible by the server. Please upload them to the server using `molclaw-file-transfer` before execution. 
- For PDB file inputs, it is recommended to preprocess them using `molclaw-pdbfixer` before execution.
- Please refer to skill `molclaw-scp-server` to complete tool invocation.

The description of tool *pepinvent_peptide_sampling_by_peptide*.

```tex
Generate new peptide molecules sampling from the input peptide sequence.
Args:
    peptide (str): SMILES representation of a peptide sequence, with amino acid residues separated by '|?|', e.g., 'N[C@@H](CCCCN)C(=O)|?|N[C@@H](CC(C)C)C(=O)|?|N[C@@H](CCCNC(=N)N)C(=O)' 
    n (int): Number of molecules for sampling
    filter_preset (str): Required filter preset; options: ['none', 'minimal', 'default', 'strict'] (commonly 'default')
    mw_min (float): Required minimum molecular weight (use 0.0 for no lower bound)
    mw_max (float): Required maximum molecular weight (use 0.0 for no upper bound)
Return:
    status (str): success/error
    msg (str): message
    save_smiles_file (str): Path to the saved SMILES file
    output_smiles_list (List[str]): List of generated SMILES strings
```

How to use tool *pepinvent_peptide_sampling_by_peptide* :

Invoke `mcp__DrugSDA-Tool__pepinvent_peptide_sampling_by_peptide` with the arguments documented above; use the result fields `output_smiles_list`.

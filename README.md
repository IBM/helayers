# Workloads for FHENDI [HPCA'25]
In this repository, we have provided the gatelists for each of the 16 workloads that we used in the FHENDI paper. . We also include an additional `.attrib` file that contains the multiplicative depth information for each of node in the gatelist.

The gatelist describes the FHE workload graph using a simple adjacency list format, where the first token, e.g. `ADD`, names the operation, the token(s) in `(...)` contain the target ciphertext/plaintext node, and the remainder of the tokens are the source ciphertext/plaintext nodes. Note that some lines also contain metadata information, e.g., the last token of a line describing a `ROTATE` operation is the amount of rotation applied to the slots of the ciphertext.

> We have removed lines starting with `GROUP` and `PARAM` as these are not fundamentally required for performance evaluation of these workloads.

## Citing
If you found these workloads to be useful for your research, please drop a citation to the following two papers.

```
@article{aharoni2023helayers,
   title     = {HeLayers: A Tile Tensors Framework for Large Neural Networks on Encrypted Data},
   volume    = {2023},
   ISSN      = {2299-0984},
   url       = {http://dx.doi.org/10.56553/popets-2023-0020},
   DOI       = {10.56553/popets-2023-0020},
   number    = {1},
   journal   = {Proceedings on Privacy Enhancing Technologies},
   publisher = {Privacy Enhancing Technologies Symposium Advisory Board},
   author    = {Aharoni, Ehud and Adir, Allon and Baruch, Moran and Drucker, Nir and Ezov, Gilad and Farkash, Ariel and Greenberg, Lev and Masalha, Ramy and Moshkowich, Guy and Murik, Dov and Shaul, Hayim and Soceanu, Omri},
   year      = {2023},
   month     = jan,
   pages     = {325–342}
}
```

```
@inproceedings{park2025fhendi,
  author     = {Park, Yongmo and Amarnath, Aporva and Pal, Subhankar and Swaminathan, Karthik V. and Buyuktosunoglu, Alper and Shaul, Hayim and Aharoni, Ehud and Drucker, Nir and D. Lu, Wei and  Soceanu, Omri and Bose, Pradip},
  title      = {FHENDI: A Near-DRAM Accelerator for Compiler-Generated Fully Homomorphic Encryption Applications},
  booktitle  = {{IEEE} International Symposium on High-Performance Computer Architecture (HPCA) 2025, Las Vegas, NV, USA, March 1-5, 2025},
  publisher  = {IEEE},
  year       = {2025, to appear}
  url        = {},
  DOI        = {},
}
```
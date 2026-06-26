# HElayers

## Scope

IBM HElayers is software development kit (SDK) for the practical and efficient
execution of encrypted workloads using fully homomorphic encrypted data.
HElayers is designed to enable application developers and data scientists to
seamlessly apply advanced privacy preserving techniques without requiring
specialized skills in cryptography.

HElayers now powers [IBM's FHE Cloud Service](https://he4cloud.com/public/), a
beta cloud service that enables data scientists and developers to deploy
privacy preserving machine learning driven Software-as-a-Service (SaaS)
applications in the Cloud.

## Usage

### Python API with helayers-pylab Docker image

Use the [`ibmcom/helayers-pylab`](https://hub.docker.com/r/ibmcom/helayers-pylab)
Docker image to explore and use HElayers using a Python API.

Use the [`ibmcom/helayers-pylab-s390x`](https://hub.docker.com/r/ibmcom/helayers-pylab-s390x)
Docker image to explore and use HElayers using a Python API on IBM Z and IBM
LinuxONE.

### C++ API with helayers-lab Docker image

Use the [`ibmcom/helayers-lab`](https://hub.docker.com/r/ibmcom/helayers-lab)
Docker image to explore and use HElayers using C++ API.

Use the [`ibmcom/helayers-lab-s390x`](https://hub.docker.com/r/ibmcom/helayers-lab-s390x)
Docker image to explore and use HElayers using C++ API on IBM Z and IBM
LinuxONE.

### pyhelayers Python package

Install the [pyhelayers](https://pypi.org/project/pyhelayers/) Python package:

    pip install pyhelayers

This is currently supported on Linux only (x86 and IBM Z).

### pyhelayerslite Python package

Install the [pyhelayerslite](https://pypi.org/project/pyhelayerslite/) Python package:

    pip install pyhelayerslite

This is currently supported on Windows only.

## License

HElayers is provided under a community edition license for non-commercial use;
see [license](https://ibm.ent.box.com/s/zfl6rt2p09811nyy8yow8t3mpsmkmsw6). For
commercial deployments and access to the source code, please contact
[chamliam@ie.ibm.com](mailto:chamliam@ie.ibm.com) for the Premium Edition
license.

## Citing IBM HELayers

To cite IBM HELayers, please use:

> Aharoni, E., Adir, A., Baruch, M., Drucker, N., Ezov, G., Farkash, A., Greenberg, L., Masalha, R., Moshkowich, G., Murik, D. and Shaul, H., 2020. HeLayers: A Tile Tensors Framework for Large Neural Networks on Encrypted Data. (2023), Privacy Enhancing Technology Symposium (PETs) 2023 (To be published)

Bibtex:

```
@article{helayers,
  author = {Aharoni, Ehud and Adir, Allon and Baruch, Moran and Drucker, Nir and Ezov, Gilad and Farkash, Ariel and Greenberg, Lev and Masalha, Ramy and Moshkowich, Guy and Murik, Dov and Shaul, Hayim and Soceanu, Omri},
  journal = {Privacy Enhancing Technology Symposium (PETs) 2023},
  title = {{HeLayers: A Tile Tensors Framework for Large Neural Networks on Encrypted Data}},
  url = {https://petsymposium.org/2023/paperlist.php},
  year = {2023}
}
```

## Support

For questions and comments about HElayers please visit our slack channel <i>#helayers</i> on [IBM AIF360 workspace](https://join.slack.com/t/aif360/shared_invite/zt-5hfvuafo-X0~g6tgJQ~7tIAT~S294TQ).

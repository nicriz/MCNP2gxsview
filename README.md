# MCNP2gxsview

### Description 
Simple internal script to correct MCNP6.2 input files so that they are readable by [Gxsview](https://www.nmri.go.jp/study/research_organization/risk/gxsview/en/top/).

### Getting Started
Clone the repository locally, the executable is in MCNP2gxsview/dist/MCNP2gxsview/MCNP2gxsview. It is reccomended to add it to your `PATH`:
```bash
export PATH="path/to/MCNP2gxsview/dist/MCNP2gxsview:$PATH"
```
To modify a MCNP input file `inp` simply run:
```bash
MCNP2gxsview inp
```
The output file is called `inp_gxs`

### Testing
The executable was produced with pyintaller and it has been tested on a Linux environment with Gxsview ver 2022.05.07.

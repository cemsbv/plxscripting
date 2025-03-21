# plxscripting

Python files required to interact with PLAXIS API. These files are created by
Seequent/Bentley (owner of PLAXIS) and distributed as part of the PLAXIS
installation. The goal of this repository is simply to store this files to ease
the CEMS development pipeline.

# Installation

To install simply run:

```
$ pip install plxscripting
```

Or for a particular version (e.g. 1.0.2):

```
$ pip install plxscripting==1.0.2
```

# Compatibility tables between Plaxis program version and repo version

Each version of this repository is compatible with one (or more) versions of 
the PLAXIS 2D and 3D programs. Below you find the table containing the 
known compatibilities, so you can install the version you need depending on
the PLAXIS program you need to use.

| Repository Version |            PLAXIS Versions             |
| :----------------: | :------------------------------------: |
|    1.0.2           | PLAXIS 2D CONNECT Edition V22 Update 2 |
|    1.0.4           | PLAXIS 2D 2023.2 , PLAXIS 3D 2023.2    | 


# Contribution

## Developer's note

Every time a new PLAXIS version is released, a new version of the
`plxscripting` directory and the `encryption.py` file is released/included in
the PLAXIS installation. Theses files are typically located under a directory similar to:

```
C:\ProgramData\Seequent\PLAXIS Python Distribution V2\python\Lib\site-packages
```

where `Seequent` used to be named `Bentley` in the previous versions and `V2`
will have a different index.

The contribution of this repository restricts itself to:
-   Copy these files to the `plxscripting` directory and the `encryption.py` under
    the `src` of this repository.
- Make a new release using the same version as in the file `plxscripting\__version__.py`.
- Updating the compatibilty tables writter in the previous section.

## Environment

We recommend developing in Python3.9 with a clean virtual environment (using `virtualenv` or `conda`), 
installing the requirements from the requirements.txt file:

Example using `virtualenv` and `pip` to install the dependencies in a new environment .env on Linux:

```bash
python -m venv .env
source .env/bin/activate
python -m pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install -e .
```

## Requirements

Requirements are autogenerated by the `pip-compile` command with python 3.9

Install pip-tools with:

```bash
pip install pip-tools
```

Generate requirements.txt file with:

```bash
pip-compile --extra=test --output-file=requirements.txt pyproject.toml
```

Update the requirements within the defined ranges with:

```bash
pip-compile --upgrade --extra=test --output-file=requirements.txt pyproject.toml
```
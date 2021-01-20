# python_package_template
This repository contains a Python package template for researchers. The parent folder, ```/python_package_template/```, contains the code necessary to install the package via pip. 

- setup.py: the install script used by pip, called with pip3 install -e .
- setup.cfg: contains the setup.py configuration information such as author contacts, package name, and version.
   

## Installation
Run these shell commands to install the dependencies into a virtual 
environment and configure the SAMPEX data paths:

```
# cd into the top project directory
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 -m microburst_ann init # and answer the promps.
```
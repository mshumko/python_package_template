# python_package_template
This repository contains a Python package template for researchers. The ```/package/``` template folder should be renamed to the package that you want imported. 

The parent folder, ```/python_package_template/```, contains the code necessary to install the package via pip:
- setup.py: the install script used by pip, called with ```pip3 install -e .```, or if you have multiple python versions installed, you can call a specific pip install via ```python3.8 -m pip install -e .``` to install this package in Python3.8.
- setup.cfg: contains the setup.py configuration information such as author contacts, package name, package version, and minimal dependencies.
- requirements.txt: typically specifies more exact dependencies than in setup.cfg. This file is useful to reproduce the development environment exactly. Consider that if this package becomes a dependency itself the exact dependencies may be too restrictive and may not correctly install. This file is usually created via ```python3 -m pip freeze > requirements.txt```. You can use pip to install these exact dependencies with ```python3 pip install -r requirements.txt```.

The package folder, ```/python_package_template/package/``` contains two template modules.
- ```__init__.py```: the module that signifies to python that the ```package/``` folder is a package. Once installed, it is imported with ```import package```. This module can contain code to run on import, such as importing other programs in the package. For example, if you have a script in ```package/visualization/make_plot.py``` containing a ```plot()``` function. If ```__init__.py``` is empty, the user can import ```plot()``` with, for example, ```from package.visualization.make_plot import plot```. This is very long to type, so the ```__init__.py``` module can contain that import as well, so the user can import ```plot()``` via ```import package.plot```. This is very flexible.
- ```__main__.py```: an optional module that creates a ```config.py``` file that contains paths to this package and any external data sources. This avoids hard-coding paths in the source code, and makes the code easily sharable. This module is executed via ```python3 -m package init```.
   
## Installation
Run these shell commands to install the dependencies into a virtual environment and configure the data paths:

```
# cd into the top directory
python3 -m venv env
source env/bin/activate

python3.8 -m pip install -e .  # (don't forget the .)
#  or 
pip3 install -r requirements.txt

python3 -m package init # and answer the promps.
```
**Graphos** is a webservice for handling dynamic graphics generation. It aims to create something close to Google Charts, in open source way.
The system is based on the excellent library [PyGal](http://pygal.org/) and can, like PyGal does, generate SVG or PNG files.


# Installation

The system use Python (tested on 2.7.3). And nothing else.


## Dependencies

The following packages are mandatory:
  * tornado: the Python server to handle incomming requests
  * lxml: needed for PyGal
  * PyGal: the SVG generator

To handle PNG support:
  * CairoSVG
  * tinycss
  * cssselect

The optional package may help:
  * Cython (tinycss try to use it)

on CentOS:
'Global' packages:
```
yum -y install python python-devel python-setuptools python-pip
```
Then, the packages for PyGal (most of them should already be installed by default):
```
yum -y python-lxml Cython cairo pycairo python-cairosvg
```
Then:
```
pip install tornado pygal tinycss cssselect
```


# Configure

You can easily configure application entry point threw ```config.ini``` file. It helps to maintain both debug and release configuration, including log configuration. Setup this file will be enough.


# Usage
Run python, and that's it: ```python server.py```
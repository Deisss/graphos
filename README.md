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

## Installing on CentOS
### 'Global' packages
```
yum -y install python python-devel python-setuptools python-pip
```
### Pygal packages
(most of them should already be installed by default):
```
yum -y python-lxml Cython cairo pycairo python-cairosvg
```
### Final dependencies threw PIP:
```
pip install tornado pygal tinycss cssselect
```


# Configure

You can easily configure application entry point threw ```config.ini``` file. It helps to maintain both debug and release configuration, including log configuration. Setup this file will be enough.


# Usage

Run python, and that's it: ```python server.py```, by default the system will start on port ```8591```.

You need to follow the [PyGal documentation](http://pygal.org/documentation/) to understand how to build URLs:
  * The chart type is always mandatory: ```&chart=Radar```
  * every options start with a 'o' before, like if you want to setup the ```fill``` property, we do: ```&ofill=true```
  * There is one exception: the ```style``` property is used directly: ```&style=DarkSolarizedStyle```
  * By default, the system will output in SVG mode, to change it to png, add the ```&output=png```
  * Finally, the series are passed like this: ```&s1=MySeries:1,2,3,4,5```, the name ```s1``` has to be unique, and start with a *s*. Anything starting with a *s* except *style*, will be consider as a serie. Then you specify the serie name (here: MySeries), and then every value separated by ','

Few examples to try:
  * Line chart with range 0 to 100: [Try it!](http://localhost:8591/?chart=Line&s1=MaSuite:1,2,3,4,5&s2=SecondSuite:2,10,4,5,12&owidth=600&oheight=400&oexplicit_size=true&ofill=true&style=DarkSolarizedStyle&orange=0,100)
  * Radar chart with style setted: [Try it!](http://localhost:8591/?chart=Radar&s1=MaSuite:1,2,3,4,5&s2=SecondSuite:2,10,4,5,12&owidth=600&oheight=400&oexplicit_size=true&ofill=true&style=DarkSolarizedStyle)
  * PNG output: [Try it!](http://localhost:8591/?chart=Radar&s1=MaSuite:1,2,3,4,5&s2=SecondSuite:2,10,4,5,12&ofill=true&output=png)


# Limitations (soon resolved)
  * For now, graphics using something else than integer/float values cannot be processed, like world map charts. Soon it will be able to process them as well.
  * the option ```interpolation_parameters``` is not handled at all
  * the option ```secondary``` for a series is not handled at all
  * The system should be able to handle something like 'range(10, 20)' to create a python range instead of specifying each values on request parameters...
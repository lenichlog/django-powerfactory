# django-powerfactory
### Test of interaction between PF and Django project.

This project was devoped to test different options of connecting Power Factory lib and Django based application.
Main problem with whis combination is inability of PF to work in more than one thread and default miltithreading Django behavier.
Django-powerfactory is an exmaple of how to bypass these incompatibilities. 


## INSTALLATION 

`git clone https://github.com/lenichlog/django-powerfactory`

## REQUIREMENTS

The minimum requirements by django-powerfactory are:

- python 3.4
- django 2.0.0
- PowerFactory v2016 SP4

## QUICK START

In file __buses/backend/pf.py__ :

1. set path to PowerFactory python lib

  example:    `LIB_PATH = "C:\\Program Files\\DIgSILENT\\PowerFactory 2016 SP4\\Python\\3.4"`

2. set path to yor project

  example:    `PROJECT_PATH = "\gurkov_lo.IntUser\Богучанская ГЭС.IntPrj"`

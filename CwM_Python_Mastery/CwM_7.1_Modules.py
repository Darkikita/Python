# Modules
#   - Creating Modules
#   - Compiled Python Files
#   - Module Search Path
#   - Packages
#   - Sub-packages
#   - Intra-package References
#   - The dir Function


#------------------------------------------------------------------------------
# Creating Modules

#CmW_Module_Sales.py

from CwM_Module_Sales import calc_tax                   #Strg + Leerzeichen

from CwM_Module_Sales import calc_tax, calc_shipping 

from CwM_Module_Sales import *                          # bad practice

calc_shipping

#-----

import CwM_Module_Sales

CwM_Module_Sales.calc_shipping


#------------------------------------------------------------------------------
# Compiled Python Files


#------------------------------------------------------------------------------
# Module Search Path

import sys

print(sys.path)


#------------------------------------------------------------------------------
# Packages

from CwM_Module_Direct.CwM_Module_sales2 import calc_volume

from CwM_Module_Direct import CwM_Module_sales2

CwM_Module_sales2.calc_volume


#------------------------------------------------------------------------------
# Sub-packages

from CwM_Module_Direct.Subpackage_Folder.CwM_Module_sales3 import calc_win

from CwM_Module_Direct.Subpackage_Folder import CwM_Module_sales3


#------------------------------------------------------------------------------
# Intra-package References

# from ..customer import sales.py



#------------------------------------------------------------------------------
# The dir Function


from CwM_Module_Direct import CwM_Module_sales2

print(dir(CwM_Module_sales2))

#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__', 'calc_volume']

print(CwM_Module_sales2.__name__)
print(CwM_Module_sales2.__package__)
print(CwM_Module_sales2.__file__)

#Ausgabe:
# CwM_Module_Direct.CwM_Module_sales2
# CwM_Module_Direct
# c:\Users\nikita.dakhno\SynologyDrive\Nikita\Python\Code\Starter\CwM_Module_Direct\CwM_Module_sales2.py'



#------------------------------------------------------------------------------
# Executing Modules as Scripts

from CwM_Module_Direct import CwM_Module_sales2

# Ausgabe: 
# Skript running
# __init__.py


# the __name__ function will call the name of the module 
# within the same module it will be __main__

#look in CwM_Module_sales2.py

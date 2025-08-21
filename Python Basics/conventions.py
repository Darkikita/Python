##########################################################################################
# Python Conventions --------------------------
##########################################################################################
print("Python Conventions")

##########################################################################################
# Variable names (snake_case)
##########################################################################################
# 1 Rule: discriptive and meaningfull variable names
# 2 Rule: lower case letters
# 3 Rule: use underscore
# 4 Rule: space around equal sign (Pep8 Autocorrect)

user_name = "Alice"
max_value = 100
print(user_name, max_value)

# Constants (UPPER_CASE)
PI = 3.14159
MAX_CONNECTIONS = 10
print(PI, MAX_CONNECTIONS)


# Functions (snake_case)
def calculate_area(radius):
    """Calculate area of a circle"""
    return PI * radius**2


print(calculate_area(5))


##########################################################################################
# Classes (PascalCase)
##########################################################################################
class BankAccount:
    """Example class"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


account = BankAccount("Alice", 100)
print(account.owner, account.balance)

##########################################################################################
# Module/File
##########################################################################################
# Module/File names: lowercase_with_underscores
# Example: my_module.py

##########################################################################################
# Indentation: always 4 spaces
##########################################################################################
x = 1
if x > 0:
    print("Positive")  # 4 spaces indent

##########################################################################################
# Imports: standard -> third-party -> local
##########################################################################################
import os
import sys
# import numpy as np   # example third-party
# import my_module     # example local module

##########################################################################################
# Boolean values: capitalized
##########################################################################################
print(True, False, None)

##########################################################################################
# Private variables: underscore prefix
##########################################################################################
_cache = {}
print(_cache)


##########################################################################################
# Very private (name mangling): double underscore
##########################################################################################
class Example:
    def __init__(self):
        self.__secret = "hidden"


obj = Example()
print(type(obj))

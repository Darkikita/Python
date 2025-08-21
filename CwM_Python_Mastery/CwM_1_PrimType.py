# Primitive Types
    # - Variables
    # - Variable Names
    # - Strings
    # - Escape Sequences
    # - Formatted Strings
    # - String Methods
    # - Numbers
    # - Working with Numbers
    # - Type Conversion



#------------------------------------------------------------------------------
# Variables

students_count = 1000
print(students_count)
#Python alocattes some memory and store that number 
#in that memory space

#Build in primitve Types in Python
#number
integer = 10     
float = 4.99 
#string
string = "Text" 
#boolean
boolean = True
#boolea True & False (big first Letter)


#------------------------------------------------------------------------------
# Variable Names

course_name = "Python Programming" 
# 1 Rule: discriptive and meaningfull variable names
# 2 Rule: lower case letters
# 3 Rule: use underscore
# 4 Rule: space around equal sign (Pep8 Autocorrect)

#------------------------------------------------------------------------------
# Strings

course_name = "Python Programming" 
course_name = 'Python Programming'

message =   """Hi John 
this is Nikita from ....

Sincerly"""

print(message)

print(len(course_name))

course = "Python"

#braket notation
print(course[0]) 
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

#------------------------------------------------------------------------------
# Escape Sequence

course = 'Python "Hallo"'
print(course)
course = "Python \"Hallo\""
print(course)
course = "Python \'Hallo\'"
print(course)
course = "Python \\Hallo\\"

#------------------------------------------------------------------------------
# Formatted Strings

first = "Nikita"
last = "Dakhno"
full1 = first + " " + last 
full2 = f"{first} {last}"
full3 = f"{len(first)} {2+2}"

print(full1)
print(full2)
print(full3)

#------------------------------------------------------------------------------
# String Methods: bulid in functions

course = "Python Programming"

len(course)
print(len(course))

course.upper()
print(course)
print(course.upper())

course = "python programming"
print(course.title())

course = " Python Programming"

print(course)
print(course.strip())
print(course.rstrip())
print(course.lstrip())

course = "Python Programming"
print(course.find("x"))     # doesnt exist in the String (-1)
print(course.find("P"))     # returns index
print(course.replace("P", "N"))
print("Pro" in course)      # find returns index, in returns boolean

#------------------------------------------------------------------------------
# Numbers

x = 1           #integer
x = 1.1         #float
x = 1 + 2j      #complex numbers

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  #if an integer is needed
print(10 % 3)
print(10 ** 3)  #Exponent

y = 5
y += 3          #Augmentet Assignment
print(y) 

# build in functions
print(round(2.9))
print(abs(-2.9))

import math

print(math.ceil(2.2))

#------------------------------------------------------------------------------
#Type Conversion

x = "Hallo"
#y = x + 1           #TypeError: can only concatenate str (not "int") to str
print(type(x))

# Casting
# int(x)
# float(x)
# bool(x)
# str(x)

x = input("x: ")
y = int(x) + 1
print(f"x: {x} y: {y}")

#Boolean False: "" ; 0 ; None
print(bool(""))
print(bool("False"))
print(bool(-1))
print(bool(5))
print(bool(None))


a = 4.0
print(type(a)) 

b = str(a)
print(type(b)) 

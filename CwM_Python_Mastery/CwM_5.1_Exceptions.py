# Exceptions
#   - Exceptions
#   - Handling Exceptions
#   - Cleaning Up
#   - The With Statement
#   - Raising Exceptions
#   - Cost of Raising Exceptions


#------------------------------------------------------------------------------
# Exceptions

numbers = [1, 2]
#print(numbers[3])

# Traceback (most recent call last):
#   File "c:\Users\nikita.dakhno\SynologyDrive\Nikita\Python\Code\Starter\CwM_5.1_Exceptions.py", line 13, in <module>
#     print(numbers[3])
#           ~~~~~~~^^^
# IndexError: list index out of range

age = int(input("Age: "))

# we input an "a"

# Traceback (most recent call last):
#   File "c:\Users\nikita.dakhno\SynologyDrive\Nikita\Python\Code\Starter\CwM_5.1_Exceptions.py", line 21, in <module>
#     age = int(input("Age: "))
#           ^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'a'


#------------------------------------------------------------------------------
# Handling Exceptions

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues")

# ex is just a name for a Variable that holds the ValueError



#------------------------------------------------------------------------------
# Handling Different Exceptions


try:
    age = int(input("Age: "))
    xfacor = 10 / age
except ValueError as ex:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")


# Age: 0
# Traceback (most recent call last):
#   File "c:\Users\nikita.dakhno\SynologyDrive\Nikita\Python\Code\Starter\test.py", line 3, in <module>
#     xfacor = 10 / age
#              ~~~^~~~~
# ZeroDivisionError: division by zero


try:
    age = int(input("Age: "))
    xfacor = 10 / age
except ValueError as ex:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exceptions were thrown")



try:
    age = int(input("Age: "))
    xfacor = 10 / age
except (ValueError, ZeroDivisionError) as ex:   #Same as the code above
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")



#------------------------------------------------------------------------------
# Cleaning Up


try:
    file = open("CwM_file.txt")
    age = int(input("Age: "))
    xfacor = 10 / age
#    file.close()                #if an error occures, this line will be oversteped
except (ValueError, ZeroDivisionError) as ex:   
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()                # Solution


#------------------------------------------------------------------------------
# The With Statement

try:
    with open("CwM_file.txt") as file:
        print("File opened")
        file.__enter__
    age = int(input("Age: "))
    xfacor = 10 / age
except (ValueError, ZeroDivisionError) as ex:   
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")

# Whenever we open a File using the wih-Statement Python will automatically
# call file.close(). 
# In other words: The with-Statement automatically releases external recources

# if a file. has two important magic methods __enter and __exit we can use the with-Statement



try:
    with open("CwM_File.txt") as fil, open("CwM_File2.txt") as target:  #no second File
        print("File opened")
    age = int(input("Age: "))
    xfacor = 10 / age
except (ValueError, ZeroDivisionError) as ex:   
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")



#------------------------------------------------------------------------------
# Raising Exceptions

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
 print(error)



#------------------------------------------------------------------------------
# Cost of Raising Exceptions


from timeit import timeit


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
 print(error)
"""

print(timeit(code1, number=10000))  #0.7245132999960333


code2= """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass                    #cannot have a empty except Block
"""

print(timeit(code2, number=10000))  # 0.003316599875688553



code3= """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print(timeit(code3, number=10000))  # 0.0013153997715562582
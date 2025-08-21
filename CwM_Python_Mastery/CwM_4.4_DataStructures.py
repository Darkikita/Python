# Data Structures
#   - Queues
#   - Tuples
#   - Swapping Variables
#   - Arrays



#------------------------------------------------------------------------------
# Queues

# FIFO: First in - First out
# if i remove an item from the front, every item after has to be shifted forward

# from Module "collections" we import the class "deque"
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

queue.popleft()     #popleft() is a Method of the deque class

print(queue)

if not queue:
    print("empty")


#------------------------------------------------------------------------------
# Tuples

# Tuple is basically a read-only-List

#Tuple definition, dont use the name "tuple"

tup = (1, 2)  
tup2 = 1, 2   
tup3 = 1,     
tup4 = ()

print(type(tup))
print(type(tup2))
print(type(tup3))
print(type(tup4))



tuple_conc = (1, 2) + (3, 4)    #Tuple concatination
print(tuple_conc)

tuple_conc2 = tup + tup2        #Tuple concatination
print(tuple_conc2)

tuple_mult = (1, 2) * 5         #Tuple creation
print(tuple_mult)


list_tuple = tuple([1, 2, 3])   #List to Tuple, call tuple function

example_tuple = (1, 2, 3, 4, 5, 6, 7)
print(example_tuple[0])         # access tuple
print(example_tuple[0:4])
print(example_tuple[:])

a, b, c, d, e, f, g = example_tuple         # unpacking a tuple

if 5 in example_tuple:          # searching for an item
    print("exists")

# example_tuple[1] = 10     TypeError: 'tuple' object does not support item assignment



#------------------------------------------------------------------------------
# Swapping Variables

x = 10
y = 11
print(x, y)

a = x
x = y
y = a
print(x, y)

#---
print("in one line")
x = 10
y = 11
print(x, y)

x, y = y, x             #swapping variables in one line
x, y = (y, x)           #y, x are a tuple
x, y = (11, 10) 
print(x, y)

a, b, c = 12, 13, 14    #multiple variable declaration
print(a, b, c)



#------------------------------------------------------------------------------
# Arrays: For performace Problems

# from Module import Class
from array import array

numbers = array("i", [1, 2, 3])       # Typecode (Google): "i" = signed integer
print(numbers)

numbers.append(4)
numbers.insert(2, 5)
print(numbers)

numbers.pop()
numbers.remove(5)
print(numbers)

numbers[1] = 5      # arrays are typed, so only integers in this case
print(numbers)


# Eigenexperiment
numbers2 = array("i", [])
print(numbers2)

# numbers2[0] = 1      IndexError: array assignment index out of range
# numbers2.append("a") TypeError: 'str' object cannot be interpreted as an integer

numbers2.append(1)
print(numbers2)
numbers2[0] = 2
print(numbers2)


# Data Structures
#   - Sets
#   - Dictionaries
#   - Dictionary Comprehensions
#   - Generator Expressions



#------------------------------------------------------------------------------
# Sets:     unordered Collection with no duplicates

numbers = [1, 1, 2, 3, 3, 4]
uniques = set(numbers)

print("numbers: ", numbers)
print("uniques: ", uniques)

second_set = {1, 4}         # {1, 4, 4}
second_set.add(5)
print(second_set)

second_set.remove(5)
print(second_set)

print(len(second_set))


#Mathematical Operations

numbers = [1, 1, 2, 3, 3, 4]

first = set(numbers)
second = {1, 4, 7, 8}

print(first | second)   # both sets combined

print(first & second)   # only items that are in both sets

print(first - second)   # all itmes that are in "first" but not in "second"

print(first ^ second)   # all items that are exclusivly in "first" or the "second" set

# print(first[0])         TypeError: 'set' object is not subscriptable (No indexing in sets)

if 1 in first:
    print("yes 1 is in first")



#------------------------------------------------------------------------------
# Dictionaries:  Key-Value Pairs

dic_1 = {}
dic_1 = {"x": 1, "y": 2}     # Key = String, Value = Integer

dic_2 = dict(x=1, y=2)
print(dic_2["x"])

dic_2["x"] = 10
print(dic_2["x"])

dic_2["z"] = 3
print(dic_2)

#print(dic_2["a"])       KeyError: 'a'

if "a" in dic_2:
    print(dic_2["a"])

if 3 in dic_2:              # cannot serach for values
    print("3 is in dic_2")

print(dic_2.get("a"))
print(dic_2.get("a", 0))    # if not found return 0 as a default
print(dic_2.get("a", "net gefunden"))    # if not found return "net gefunden" as a default
print(dic_2.get("x"))

print(dic_2)
del dic_2["z"]
print(dic_2)

# Loop over dictonaries

for key in dic_2:
    print(key, "->", dic_2[key])

for key in dic_2.items():
    print(key)



#------------------------------------------------------------------------------
# Dictionary Comprehensions

values = []

print(values) # []
# expression for item in items
for x in range(5):
    values.append(x * 2) 
print(values) # [0, 2, 4, 6, 8]


list_nd = []
print(list_nd)
list_nd = [x * 2 for x in range(5)]
print(list_nd)


# set_nd = {}
set_nd = {x * 2 for x in range(5)}
print(set_nd)


dict_nd = {}
dict_nd = {x: x * 2 for x in range(5)}  #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
print(dict_nd)

dict_nd = {x: x * 2 for x in range(10, 15)}
print(dict_nd)

dict_nd = {x: x * 2 for x in range(0, 10, 2)}
print(dict_nd)

#ChatGBT
import string

dict_nd = {letter: i * 2 for i, letter in enumerate(string.ascii_lowercase[:5])}
print(dict_nd)



#------------------------------------------------------------------------------
# Generator Expressions

tuple_nd = (x * 2 for x in range(5)) 
print(tuple_nd) # <generator object <genexpr> at 0x000001FAAFFC05F0>


list_values = [x * 2 for x in range(10)]
for x in list_values: 
    print(x)

# Problem: what is we have 1.000.000 objects in memory, storing them in list_values would be inefficient
# Solution: Generator Objects: they are iterable, in each itteration they generate a new value, they dont store


gen_values = (x * 2 for x in range(10))
print(gen_values)
for x in gen_values: 
    print(x)


from sys import getsizeof

gen_values2 = (x * 2 for x in range(1000))
print(gen_values2)
print(getsizeof(gen_values2))   # range(1000) = 208; range(100000) = 208

list_values2 = [x * 2 for x in range(100000)]
print(getsizeof(list_values2))  # range(1000) = 8856; range(100000) = 800984


# print(len(gen_values)) TypeError: object of type 'generator' has no len()
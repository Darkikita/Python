##########################################################################################
# List
##########################################################################################
# -----------------------------------------------------------------
# List properties:
# mutable        → elements can be changed after creation
# ordered        → keeps the insertion order
# duplicates     → allows duplicate values
# indexable      → access by index (positive/negative)
# sliceable      → supports slicing with [start:end:step]
# heterogeneous  → can contain mixed data types
# iterable       → can be used in loops (for, while, comprehensions)
# dynamic size   → can grow and shrink (append, remove, etc.)
# -----------------------------------------------------------------
# Common list methods:
# append(x)        → add item at the end
# insert(i, x)     → insert item at index i
# remove(x)        → remove first occurrence of x
# pop([i])         → remove and return item at index i (default last)
# clear()          → remove all items
# index(x)         → return index of first occurrence of x
# count(x)         → return number of occurrences of x
# sort()           → sort list in place
# reverse()        → reverse list in place
# copy()           → shallow copy of list
# extend(iterable) → add all elements from another iterable
# -----------------------------------------------------------------
print("List")

# mutable (changeable), ordered, allows duplicates
fruits = ["apple", "banana", "cherry"]
print(fruits)

# access elements
print(fruits[0])  # apple
print(fruits[-1])  # cherry
print(fruits[0:2])  # ['apple', 'banana']

# modify
fruits[1] = "blueberry"
print(fruits)  # -> ['apple', 'blueberry', 'cherry']

# add & remove
fruits.append("orange")  # add at end -> ["apple", "banana", "cherry"]
fruits.insert(1, "pear")  # insert at index
print(fruits)  # -> ['apple', 'pear', 'blueberry', 'cherry', 'orange']

fruits.remove("apple")  # remove by value
print(fruits.pop())  # remove last and return
print(fruits)

# check existence
print("cherry" in fruits)  # True

# length
print(len(fruits))  # number of items

# list comprehension
squares = [x**2 for x in range(5)]
print(squares)

# List Methods ---------------------------------------------------
print("List Methods")

lst = [3, 1, 4, 1, 5]

# append(x) → add item at the end
lst.append(9)
print(lst)  # [3, 1, 4, 1, 5, 9]

# insert(i, x) → insert item at index i
lst.insert(2, 7)
print(lst)  # [3, 1, 7, 4, 1, 5, 9]

# remove(x) → remove first occurrence of x
lst.remove(1)
print(lst)  # [3, 7, 4, 1, 5, 9]

# pop([i]) → remove and return item at index i (default last)
print(lst.pop())  # 9
print(lst)  # [3, 7, 4, 1, 5]
print(lst.pop(2))  # 4
print(lst)  # [3, 7, 1, 5]

# clear() → remove all items
copy_lst = lst.copy()
copy_lst.clear()
print(copy_lst)  # []

# index(x) → return index of first occurrence of x
print(lst.index(7))  # 1

# count(x) → return number of occurrences of x
print(lst.count(1))  # 1

# sort() → sort list in place
unsorted = [5, 2, 9, 1]
unsorted.sort()
print(unsorted)  # [1, 2, 5, 9]

# reverse() → reverse list in place
unsorted.reverse()
print(unsorted)  # [9, 5, 2, 1]

# copy() → shallow copy of list
copy_lst = lst.copy()
print(copy_lst)  # [3, 7, 1, 5]

# extend(iterable) → add all elements from another iterable
lst.extend([10, 11])
print(lst)  # [3, 7, 1, 5, 10, 11]

##########################################################################################
# Tuple --------------------------
##########################################################################################
# -----------------------------------------------------------------
# Tuple properties:
# immutable       → cannot be changed after creation
# ordered         → keeps the insertion order
# duplicates      → allows duplicate values
# indexable       → access by index (positive/negative)
# sliceable       → supports slicing with [start:end:step]
# fixed size      → length cannot change
# hashable        → can be used as dictionary keys (lists cannot!)
# -----------------------------------------------------------------
# Common tuple methods:
# count(x)        → return number of occurrences of x
# index(x)        → return index of first occurrence of x
# -----------------------------------------------------------------
print("Tuple")

# immutable, ordered
coordinates = (10, 20)
print(coordinates)  # -> (10, 20)

# single element tuple needs a comma
single = (5,)
print(type(single))  # <class 'tuple'>

# unpacking
x, y = coordinates
print(x, y)  # -> 10, 20

##########################################################################################
# Functions for Sequences
##########################################################################################
# -----------------------------------------------------------------
# Common functions for sequences:
# len(seq)       → number of elements
# min(seq)       → smallest element
# max(seq)       → largest element
# sum(seq)       → sum of all elements (numbers only)
# sorted(seq)    → return sorted list (does not change original)
# reversed(seq)  → return reversed iterator
# -----------------------------------------------------------------
print("Common Functions")

numbers = [3, 1, 4, 1, 5, 9]

print(len(numbers))  # 6
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 23
print(sorted(numbers))  # [1, 1, 3, 4, 5, 9]
print(list(reversed(numbers)))  # [9, 5, 1, 4, 1, 3]

##########################################################################################
# Developer Functions for Sequences
##########################################################################################
# enumerate(seq)     → iterate with index and value
# zip(seq1, seq2)    → combine multiple sequences element-wise
# all(seq)           → True if all elements are truthy
# any(seq)           → True if at least one element is truthy
# map(func, seq)     → apply function to each element
# filter(func, seq)  → filter elements by condition
##########################################################################################
print("Developer Functions")

words = ["Python", "is", "fun"]

# enumerate
for i, w in enumerate(words):
    print(i, w)  # 0 Python / 1 is / 2 fun

# zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# all / any
print(all([1, 2, 3]))  # True (all non-zero)
print(all([1, 0, 3]))  # False (0 is falsy)
print(any([0, 0, 5]))  # True (at least one non-zero)

# map
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))  # [2, 4, 6]

# filter
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]

##########################################################################################
# Range
##########################################################################################
# -----------------------------------------------------------------
# Range:
# - Built-in function to create an immutable sequence of numbers
# - Syntax: range(start, stop, step)
#   • start (optional, default=0) → first number in sequence
#   • stop (required)             → sequence ends before this value
#   • step (optional, default=1)  → increment (can be negative)
# - Commonly used in loops and for generating sequences
# - Returns a range object (lazy), often converted with list()
# -----------------------------------------------------------------
print("Range")

# generates a sequence of numbers
r = range(5)  # 0,1,2,3,4
print(list(r))  # -> [0, 1, 2, 3, 4]

r2 = range(2, 10, 2)  # start, stop, step
print(list(r2))  # -> [2, 4, 6, 8]

# Range Examples ---------------------------------------------------

# Basic loop with range
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# Start and stop
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5
print()

# With step
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# Negative step (counting backwards)
for i in range(10, 0, -2):
    print(i, end=" ")  # 10 8 6 4 2
print()

# Using range with list()
nums = list(range(1, 11))
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Range in list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Range with len() to iterate indexes
words = ["Python", "is", "fun"]
for i in range(len(words)):
    print(i, words[i])  # 0 Python / 1 is / 2 fun

##########################################################################################
# String as Sequence
##########################################################################################
print("String as Sequence")

text = "Python"
print(text[0])  # P
print(text[-1])  # n
print(text[0:3])  # Pyt

# iterate
for ch in text:
    print(ch, end=" ")

# immutable → can't change directly
# text[0] = "J" → Error

# must create new string
new_text = "J" + text[1:]
print(new_text)

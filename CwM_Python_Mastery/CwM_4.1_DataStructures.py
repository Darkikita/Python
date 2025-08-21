# Data Structures
#   - Lists
#   - Accessing Items
#   - List Unpacking
#   - Looping over Lists
#   - Adding or Removing Items



#------------------------------------------------------------------------------
# Lists

numbers = [1, 2, 3]
letters = ["a", "b", "c"]
mix = ["a", 1, "b"]

for item in mix:
    print(item)


matrix = [[0,1], [2,3]]
print(matrix)

hundert_zeros = [0] * 100
print(hundert_zeros)

five_zeros = [0] * 5
five_ones = [1] * 5
combined = five_zeros + five_ones
print(combined)

twenty = list(range(20))
print(twenty)


#------------------------------------------------------------------------------
# Accessing Items

chars = list("Hello World")
print(chars)
chars[0] = "B"
print(chars)

print(chars[0:3])
print(chars[:3])
print(chars[:])
print(chars[::2]) #every second element

numbers = list(range(20))
print(numbers)
print(numbers[::2])
print(numbers[::-1])


#------------------------------------------------------------------------------
# List Unpacking

numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# thrid = numbers[2]

first, second, third = numbers

print(first, second, third)


numbers2 = [1, 2, 3, 4, 5]

first2, second2, *others = numbers2

print(first2)
print(others)

first2, *others, last = numbers2

print(first2)
print(others)
print(last)



#------------------------------------------------------------------------------
# Looping over Lists

letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

#enumerate

letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)

#list
items = [0, "a"]
index, letter = items
print(index,"-", letter)

#tupel
items = (0, "a")
index, letter = items
print(index,"-", letter)

# unpacking the enumerate tuple 
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index,"-", letter)




#------------------------------------------------------------------------------
# Adding or Removing Items


letters = ["a", "b", "c"]

#Add
 #in the end
letters.append("d")
print(letters)

 #in the middle
letters.insert(2, "x")
print(letters)

#Remove
 #in the end
letters.pop()
print(letters)

 #in the middle
letters.pop(2)
print(letters)

 #objects with unknown index
letters.remove("c")
print(letters)

 # del Statement
letters2 = ["a", "b", "c", "d", "e", "f", "g"]
del letters2[0:3]
print(letters2)

 #clear Method
letters2.clear()
print(letters2)



# Data Structures
#   - Unpacking Operator
#   - Exercise



#------------------------------------------------------------------------------
# Unpacking Operator

numbers = [1, 2, 3] 
print(numbers)          #[1, 2, 3]
print(1, 2, 3)          #1 2 3

print(*numbers)         #1 2 3


#creating lists

list_nd = list(range(5))
print(list_nd)

list_nd2 = [*range(5), *"Hello"]
print(list_nd2)


first = [1, 2]
second = [3, 4, 5]
list_nd3 = [*first, "a", *second, *"Nikita"]
print(list_nd3)


#Dictonaries
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1} # "x": 10 in second overwrites "x": 1 in first
print(combined) 



#------------------------------------------------------------------------------
# Exercise


# Version 1

x, y = 0, None
sentence = "This is a common interview question"

tuple_nd = tuple(sentence)
# print(tuple_nd)

for letter in tuple_nd:
    letter_count = tuple_nd.count(letter)
    letter_value = letter
    print("The Character", letter_value, "is included", letter_count, "times!")
    if letter_count >= x:
        x = letter_count
        y = letter_value


print("The most repeated Character in this text is", y, "included", x, "times!")




# Version 2

sentence = "This is a common interview question"
# print(tuple_nd)
dictionary_nd = {}
#print(type(dictionary_nd))

for letter in sentence.lower():
    letter_value = letter
    letter_count = sentence.count(letter)
    dictionary_nd[letter_value] = letter_count

print(dictionary_nd)

max_value = max(dictionary_nd.values())
print(max_value)

max_keys = list(filter(lambda x:x[1] == max_value, dictionary_nd.items()))
print(max_keys)


# Solution

from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
#pprint(char_frequency, width=1)

# print(sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))

char_frequency_sorted = sorted(char_frequency.items(), 
                               key=lambda kv: kv[1], 
                               reverse=True)

print(char_frequency_sorted[0])
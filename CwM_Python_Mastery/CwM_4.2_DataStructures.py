# Data Structures
#   - Finding Items
#   - Sorting Lists
#   - Lambda Functions
#   - Map Function



#------------------------------------------------------------------------------
# Finding Items

letters = ["a", "b", "c"]

print(letters.index("a"))
# print(letters.index("d")) # Error

if "d" in letters:
    print(letters.index("d"))

letters = ["a", "a", "b", "c"]
print(letters.count("a"))
print(letters.count("d"))


#------------------------------------------------------------------------------
# Sorting Lists

# sort Method
numbers = [2, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.sort(reverse=False)
print(numbers)

# sorted function (build in)
 # does not change the original list
numbers = [2, 51, 2, 8, 6]
print(sorted(numbers))

print(sorted(numbers, reverse=True))

print(numbers)


# complex obejcts
items =[
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]

items.sort()    #Python sortiert nach dem ersten Element der Tupel der List
print(items)


def sort_item(item):    # we will define a function for sorting a tuple list
    return item[1]

items.sort(key=sort_item)   # Sortierschlüssel (key) ist der return des sort_item Funktion
                            # hier wird lediglich die Referenz auf eine Funktion übergeben
print(items)



 # Fehlversuch: items wird in item übergeben 
print("funk:", sort_item(items))
 # Ausgabe ("Product2", 20) da es das zweite [1] Element ist



#------------------------------------------------------------------------------
# Lambda Functions


items =[
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]    

# Lambda does exactly what this function does
# def sort_item(item): 
#     return item[1]

# list.sort(key=lambda parameters:expression)
items.sort(key=lambda item:item[1])

print(items)




#------------------------------------------------------------------------------
# Map Function

items =[
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]   

# We want to transform this list in a List of numbers (price) only
# 1.
prices = []
for item in items:
    prices.append(item[1])

print(prices)


# 2. "A Better way"
x = map(lambda item: item[1], items)    #use list items and map/extract the item[1]

print(x)    #Ausgabe: <map object at 0x000002B87CE33D90>


# 2.1 Ausgabe über For-Schleife
for item in x:  
    print(item)

print(x)

list_object = list(x)
print(list_object)      #Leere List da x durch map ein Iterator ist, welcher nur einmal durchlaufen werden kann


# 2.2 Ausgabe über Liste
prices = map(lambda item: item[1], items)

list_object = list(prices)
print(list_object) 


# 2.2.2 list direkt über map Funktion anwenden
prices = list(map(lambda item: item[1], items))
print(prices)


#Muster
items =[
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]    

prices = list(map(lambda item: item[1], items)) 
print(prices)


##########################################################################################
# Dictionary (Mapping)
##########################################################################################
# -----------------------------------------------------------------
# Dictionary properties:
# - mutable       → can be changed after creation
# - unordered     → no fixed order (insertion order preserved since Python 3.7+)
# - unique keys   → keys must be unique, values can be duplicates
# - key types     → keys must be hashable (immutable types: str, int, tuple, etc.)
# - dynamic size  → can grow and shrink
# - iterable      → iterates over keys by default
# -----------------------------------------------------------------
# Common dictionary methods:
# keys()          → return all keys
# values()        → return all values
# items()         → return all key-value pairs
# get(key, [def]) → get value by key (default if not found)
# pop(key)        → remove key and return its value
# popitem()       → remove and return last inserted key-value pair
# update({...})   → update dictionary with another dict or iterable
# clear()         → remove all items
# copy()          → shallow copy of dictionary
# fromkeys(seq, v)→ create dict with keys from seq and value v
# -----------------------------------------------------------------
print("Dictionary")

# create dictionary
person = {"name": "Alice", "age": 30, "city": "Berlin"}
print(person)

# access values
print(person["name"])  # Alice
print(person.get("age"))  # 30
print(person.get("country", "Unknown"))  # Unknown (default)

# add / modify
person["age"] = 31
person["job"] = "Engineer"
print(person)

# remove
print(person.pop("city"))  # Berlin
print(person)

# popitem (removes last key-value)
print(person.popitem())  # e.g. ('job', 'Engineer')
print(person)

# keys, values, items
print(person.keys())  # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 31])
print(person.items())  # dict_items([('name', 'Alice'), ('age', 31)])

# update
person.update({"country": "Germany", "age": 32})
print(person)

# clear
copy_person = person.copy()
copy_person.clear()
print(copy_person)  # {}

# fromkeys
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

##########################################################################################
# Common Functions for Mappings
##########################################################################################
# len(dict)    → number of key-value pairs
# str(dict)    → string representation
# dict(...)    → create new dictionary
##########################################################################################
print("Common Functions")

d = {"x": 10, "y": 20}
print(len(d))  # 2
print(str(d))  # "{'x': 10, 'y': 20}"
print(dict(a=1, b=2))  # {'a': 1, 'b': 2}

##########################################################################################
# Iteration over Dictionary
##########################################################################################
print("Iteration")

sample = {"a": 1, "b": 2, "c": 3}

for key in sample:  # iterate keys
    print(key)

for value in sample.values():  # iterate values
    print(value)

for k, v in sample.items():  # iterate key-value pairs
    print(k, v)

#Range

for i in range(0, 20, 3):
    print(i)

#Liste

for x in [1, 2, 3, 4]:
    print(x)

my_list = [10, 20, 30]
for item in my_list:
    print(item)

#Tupel

my_tuple = (1, 2, 3)
for number in my_tuple:
    print(number)

#Sting

text = "Hallo"
for char in text:
    print(char)

#Dicrionary

my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key)  # Standardmäßig iteriert man über die Schlüssel

# Oder um Schlüssel und Werte gleichzeitig zu bekommen:
for key, value in my_dict.items():
    print(key, value)


#Set

my_set = {4, 5, 6}
for element in my_set:
    print(element)


#Dateien

with open("CwM_File.txt", "r") as file:
    for line in file:
        print(line.strip())


#Generatoren

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
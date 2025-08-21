# Functions
#   - Defining Functions
#   - Arguments
#   - Types of Functions
#   - Keyword Arguments
#   - Default Arguments
#   - xargs
#   - xxargs

#------------------------------------------------------------------------------
# Defining Functions

def greet(): 
    print("Hi there")
    print("Welcome aboard")
# 2 empty lines are recommended by PEP8
#
greet()

#------------------------------------------------------------------------------
# Arguments

def greet2(first_name, last_name): 
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


greet2("Nikita", "Dakhno")

# first_name = Parameter; "Nikita" = Argument


#------------------------------------------------------------------------------
# Types of Functions

# 2 Types of Functions: 
# -> Perform a task     (greet-Function)
# -> Return a value     (round-Function)


def get_greeting(name):
    return f"Hi {name}"


print(get_greeting("Nikita"))

message = get_greeting("Nikita")    #We can store the value
print(message)

file = open("CwM_File.txt", "w")
file.write(message)

#---

def none_func():
    print("Functions return \"None\" by default")


print(none_func())


#------------------------------------------------------------------------------
# Keyword Arguments

def increment(number, by):
    return number + by


result = increment(2,1)
print(result)

print(increment(2,1))

print(increment(number = 2, by = 1))

#------------------------------------------------------------------------------
# Default Arguments

def increment2(number, by = 1): #default value = 1
    return number + by


print(increment2(2))    # 2 + 1(default)
print(increment2(2,5))  # 2 + 5

#------------------------------------------------------------------------------
# xargs

def multiply(*numbers):
    print(numbers)

multiply(2, 3, 4, 5)


def multiply2(*numbers):
    for number in numbers:
        print(number)

multiply2(2, 3, 4, 5)


print("multiply3")

def multiply3(*numbers):
    total = 1
    for number in numbers:
        print(f"Number: {number}")
        total *= number
        print(f"Total: {total}")

multiply3(2, 3, 4, 5)



print("multiply4")

def multiply4(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply4(2, 3, 4, 5))


#------------------------------------------------------------------------------
# xxargs

def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])

save_user(id=1, name="John", age=22)

# {'id': 1, 'name': 'John', 'age': 22}  [Key: Value]-Pairs
# With xxargs you can give multiple Keywordarguments and Python will pack them into a Dictonary
# Functions
#   - Scope
#   - Exercise
#   - Solution


#------------------------------------------------------------------------------
# Scope

def greet():
    message = "a"

# Locale Variable only exists (inside this function/...) in the Scope of the Function

honorific = "Mr"    #global variable = evil

def greet2(name):   
    message = f"{honorific} {name}"
    return message

def send_email(name):               #Local Variable so no conflict with other same-named LV
    message = f"@{honorific} {name}"
    return message

# print(name)   Fehler das Lokale Variable

print(greet2("Nikita"))
print(send_email("Nikita"))

#---

letter = "a"

def change():
    letter = "b"

change()
print(letter)

#Bad Practice

def modify():
    global letter
    letter = "b"

modify()
print(letter)

#------------------------------------------------------------------------------
# Exercise 

def fizz_buzz(input):
    output = ""
    if input % 3 == 0:
        output += "fizz"
    if input % 5 == 0:
        output += "buzz"
    if (input % 3 != 0) and (input % 5 != 0): 
        output = input
    return output


print(fizz_buzz(6))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(7))


# Variable muss außerhalb von If initalisiert werden, und zumindest None sein.
# if-elif-else-Konstruktion wird nach erster Erfolgreicher abfrage überprungen
# if-if-Konstruktion wird komplett durchlaufen
# if input % 3 != 0 and input % 5 != 0: problem: wie setzte ich if not; == or ==; != and !=


#------------------------------------------------------------------------------
# Solution

def fizz_buzz_solution(input):
    if (input % 3 == 0) and (input % 5 == 0): 
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input

print(fizz_buzz_solution(6))
print(fizz_buzz_solution(10))
print(fizz_buzz_solution(15))
print(fizz_buzz_solution(7))
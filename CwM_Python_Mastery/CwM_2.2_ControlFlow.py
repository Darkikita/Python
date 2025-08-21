# Control Flow
#   - For-Loops
#   - For..Else
#   - Nested Loops
#   - Iterables
#   - While Loops
#   - Infinite Loops
#   - Exercise

#------------------------------------------------------------------------------
# For-Loops

for number in range(3):
    print("Loop", number)

for number in range(3):
    print(f"Loop: {number}")

for number in range(3):
    print("Loop", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Loop", number, number * ".")




#------------------------------------------------------------------------------
# For..Else

successful = True 
#successful = False

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:                           #only executed if loop terminated without early termination
    print("Attempted 3 times and failed")


#------------------------------------------------------------------------------
# Nested Loops

for x in range(5):
    for y in range(3):
        print(f"{x},{y}")


#------------------------------------------------------------------------------
# Iterables

print(type(5))
print(type(range(5)))

#range is a complex type
#We can itterate over range

for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in ["L1", "L2", "L3", "L4"]:
    print(x)

#------------------------------------------------------------------------------
# While Loops

number = 100
while number > 0:
    print(number)
    number //= 2    # number = number // 2

command = ""
quit_command = "quit"
while command.lower() != quit_command:
    command = input(">")
    print("ECHO", command)


#------------------------------------------------------------------------------
# Infinite Loops

command = ""
quit_command = "quit"
while True:             #run foerver without break
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break


#------------------------------------------------------------------------------
# Exercise

x = int(input("Gerade Zahlen bis:"))
count = 0

for number in range(1, x):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")    
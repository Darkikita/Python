# Control Flow
#   - Comparison Operators
#   - Conditional Statements
#   - Logical Operator
#   - Short-circut Evaluation
#   - Chaining Comparison Operators

#------------------------------------------------------------------------------
# Control Flow

if 10 <= 12:        # > ; < ; >= ; <= ; == ; =!
    print("True")
else:
    print("False")


if 10 == "10":        
    print("True")
else:
    print("False")


if "Text" == "Text":        
    print("True")
else:
    print("False")

if "bag" > "apple":        # bag comes after apple = it is bigger 
    print("True")
else:
    print("False")

if "b" == "B":        
    print("True")
else:
    print("False")

print(ord("b"))
print(ord("B"))
print(ord("."))
print(ord("a"))
print(ord(" "))

#------------------------------------------------------------------------------
# Conditional Statements

temperature = 0     # 30 ; 20

if temperature > 30:
    print("oh its hot")
elif temperature < 10:
    print("oh its cold")
else:
    print("something inbetween")
print("if is done")


#------------------------------------------------------------------------------
# Ternary Operator
age = 10 # 20

if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)

message = "eligible" if age >= 18 else "not eligible"
print(message)


#------------------------------------------------------------------------------
# Logical Operator (and, or, not)

high_income = False
good_credit = True
student = False

if high_income and good_credit:     # high_income == True is implicit
    print("eligible for loan")
else:
    print("not eligible for loan")




if not student:     
    print("eligible for loan 2")
else:
    print("not eligible for loan 2")


if (high_income or good_credit) and not student :     # high_income == True is implicit
    print("eligible for loan 3")
else:
    print("not eligible for loan 3")


if high_income or good_credit and not student:     
    print("eligible")
# if high_income is Ture or good_credit is true and student is false
# for better understanding: high_income or (good_credit and not student)


#------------------------------------------------------------------------------
# Short-circut Evaluation

high_income = False
good_credit = True
student = False


if high_income and good_credit and not student:     
    print("eligible")
# Python Interpreter stops after he evaluated high_income as False


if high_income or good_credit or not student:     
    print("eligible")
# Python Interpreter stops after he evaluated good_credit as True


#------------------------------------------------------------------------------
# Chaining Comparison Operators

# age should be between 18 and 35

age = 31

if age >= 18 and age <=35:
    print("eligible 1")

if 18 <= age <= 35:
    print("eligible 2")
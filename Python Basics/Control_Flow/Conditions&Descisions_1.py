##########################################################################################
# Conditions Basics --------------------------
##########################################################################################
# -----------------------------------------------------------------
# Comparison Operators:
# <   → less than
# <=  → less or equal
# >   → greater than
# >=  → greater or equal
# ==  → equal
# !=  → not equal
# -----------------------------------------------------------------
print("Comparison Operators")

print(3 < 5)     # True
print(10 == 10)  # True
print(7 != 8)    # True
print("a" < "b") # True (compares Unicode values)


# -----------------------------------------------------------------
# Conditional Statements:
# - if    → execute block if condition is True
# - elif  → test another condition if previous was False
# - else  → execute block if none of the above is True
# -----------------------------------------------------------------
print("Conditional Statements")

x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


# -----------------------------------------------------------------
# Ternary Operator (Conditional Expression):
# condition ? true_value : false_value   →   true_value if condition else false_value
# -----------------------------------------------------------------
print("Ternary Operator")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult


# -----------------------------------------------------------------
# Logical Operators:
# and → True if both are True
# or  → True if at least one is True
# not → inverts the condition
# -----------------------------------------------------------------
print("Logical Operators")

print(True and False)  # False
print(True or False)   # True
print(not False)       # True


# -----------------------------------------------------------------
# Short-circuit Evaluation:
# - and → stops at first False
# - or  → stops at first True
# -----------------------------------------------------------------
print("Short-circuit Evaluation")

def check(msg):
    print(msg)
    return True

print(True or check("not called"))   # True (second not evaluated)
print(False and check("not called")) # False (second not evaluated)


# -----------------------------------------------------------------
# Chaining Comparison Operators:
# Multiple comparisons combined in a single expression
# -----------------------------------------------------------------
print("Chaining Comparison Operators")

age = 25
print(18 <= age <= 35)   # True (age between 18 and 35)
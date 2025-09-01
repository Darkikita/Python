##########################################################################################
# Conditions Advanced (Part 1) --------------------------
##########################################################################################

# -----------------------------------------------------------------
# Identity vs Equality (is vs ==):
# ==  → compares values (content equality)
# is  → compares identity (same object in memory)
# Best practice: use "is" for None checks
# -----------------------------------------------------------------
print("Identity vs Equality")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)     # True  (same content)
print(a is b)     # False (different objects)
print(a is c)     # True  (same object)

x = None
print(x is None)  # True (preferred style)


# -----------------------------------------------------------------
# Truthy & Falsy Values:
# Falsy values:
#   False, None, 0, 0.0, 0j, "", [], {}, set(), range(0)
# Everything else is truthy
# -----------------------------------------------------------------
print("Truthy & Falsy Values")

print(bool(""))       # False
print(bool("Hi"))     # True
print(bool(0))        # False
print(bool(42))       # True
print(bool([]))       # False
print(bool([1, 2]))   # True


# -----------------------------------------------------------------
# Return values of and / or:
# and → returns first falsy or last value
# or  → returns first truthy or last value
# Useful for defaults, but watch out with 0 / ""
# -----------------------------------------------------------------
print("Return values of and / or")

print(0 and 5)       # 0
print(5 and 10)      # 10
print("" or "Hi")    # "Hi"
print("Yes" or "No") # "Yes"

# default value pattern
user_input = ""
name = user_input or "Anonymous"
print(name)  # Anonymous


# -----------------------------------------------------------------
# Membership Operators:
# in / not in → check if element is in a sequence, set, dict (keys)
# -----------------------------------------------------------------
print("Membership Operators")

print("a" in "apple")         # True
print("z" not in "apple")     # True
print(2 in [1, 2, 3])         # True
print("key" in {"key": 1})    # True (checks keys!)


# -----------------------------------------------------------------
# Operator Precedence & Parentheses:
# Precedence order: not > and > or
# Use parentheses to improve readability
# -----------------------------------------------------------------
print("Operator Precedence & Parentheses")

print(True or False and False)        # True (and first)
print((True or False) and False)      # False (parentheses change order)


# -----------------------------------------------------------------
# Best Practices for Ternary Expressions:
# Syntax: a if condition else b
# - Use for simple, short expressions
# - Avoid nested ternaries → use if/else blocks instead
# -----------------------------------------------------------------
print("Best Practices for Ternary Expressions")

age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)  # Minor


# -----------------------------------------------------------------
# Chained Comparisons – Pitfalls & Notes:
# Python allows chaining: a < b < c
# Equivalent to (a < b) and (b < c)
# Avoid functions with side effects in chained comparisons
# -----------------------------------------------------------------
print("Chained Comparisons – Pitfalls & Notes")

x = 5
print(1 < x < 10)        # True
print(x == 5 == True)    # False (x == 5 and 5 == True → False)
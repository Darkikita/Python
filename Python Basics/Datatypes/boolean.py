##########################################################################################
# Booleans --------------------------
##########################################################################################
print("Booleans")

# Boolean values
print(True)  # True
print(False)  # False

# Boolean from expressions
print(5 > 2)  # True
print(10 == 3)  # False
print(7 != 8)  # True

# Boolean conversion with bool()
# Falsy values in Python:
#   - False
#   - None
#   - 0 (int, float, complex)
#   - "" (empty string)
#   - [] (empty list)
#   - {} (empty dict)
#   - set() (empty set)
#   - other empty containers

print(bool(""))  # False (empty string)
print(bool("False"))  # True  (non-empty string)
print(bool(0))  # False
print(bool(-1))  # True (any non-zero number)
print(bool(5))  # True
print(bool(None))  # False

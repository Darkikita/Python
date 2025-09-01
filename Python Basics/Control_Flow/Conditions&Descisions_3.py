##########################################################################################
# Conditions Advanced (Part 2) --------------------------
##########################################################################################

# -----------------------------------------------------------------
# Floating-Point Comparisons (math.isclose):
# - Avoid direct equality with floats due to rounding errors
# - Use math.isclose(a, b, rel_tol=..., abs_tol=...) for safe comparisons
# -----------------------------------------------------------------
print("Floating-Point Comparisons")

import math

a = 0.1 + 0.2
b = 0.3
print(a == b)                          # False (surprising!)
print(math.isclose(a, b))              # True (default tolerances)
print(math.isclose(a, b, rel_tol=1e-12, abs_tol=0.0))  # True/False depending on tolerance


# -----------------------------------------------------------------
# Pattern Matching (match ... case) [Python 3.10+]:
# - Structural pattern matching for clean multi-branch logic
# - Supports literals, sequences, mappings, classes, and guards (if)
# -----------------------------------------------------------------
print("Pattern Matching")

def http_status_message(code):
    match code:
        case 200:
            return "OK"
        case 400 | 404:
            return "Client Error"
        case 500:
            return "Server Error"
        case _ if 100 <= code < 200:
            return "Informational"
        case _:
            return "Unknown"
print(http_status_message(404))        # Client Error


# -----------------------------------------------------------------
# Walrus Operator (:=) – Assignment Expressions:
# - Assign and use a value within an expression (e.g., in conditions/loops)
# - Improves performance/readability when avoiding duplicate work
# -----------------------------------------------------------------
print("Walrus Operator")

def read_tokens(src: str):
    # Example: consume tokens split by space, print until empty
    while (token := src.split(" ", 1)[0]):
        print(token)
        src = src[len(token):].lstrip()
        if not src:
            break

read_tokens("alpha beta gamma")        # alpha \n beta \n gamma


# -----------------------------------------------------------------
# De Morgan’s Laws & Negations:
# - not (A or B) == (not A) and (not B)
# - not (A and B) == (not A) or  (not B)
# - Use to simplify/clarify complex conditions
# -----------------------------------------------------------------
print("De Morgan's Laws")

A, B = True, False
left  = not (A or B)
right = (not A) and (not B)
print(left == right)                   # True


# -----------------------------------------------------------------
# Guard Clauses / Early Return:
# - Return early on invalid/edge conditions to avoid deep nesting
# - Leads to flatter, clearer code
# -----------------------------------------------------------------
print("Guard Clauses / Early Return")

def divide(a: float, b: float) -> float | None:
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a / b

print(divide(10, 2))                   # 5.0
print(divide(10, 0))                   # None with message


# -----------------------------------------------------------------
# Using all() / any() for combined conditions:
# - all(iterable) → True if all elements are truthy
# - any(iterable) → True if at least one element is truthy
# - Great with generator expressions
# -----------------------------------------------------------------
print("all() / any()")

nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))   # True (all even)
print(any(n > 7 for n in nums))        # True (at least one > 7)


# -----------------------------------------------------------------
# Common Mistakes / Anti-Patterns:
# - Using 'is' instead of '==' for value comparison (except None)
# - Confusing bitwise & | with logical and or
# - Overusing nested ternaries → hurts readability
# - Overly complex conditions without parentheses
# -----------------------------------------------------------------
print("Common Mistakes / Anti-Patterns")

# 'is' vs '=='
s1 = "hello"
s2 = "he" + "llo"
print(s1 == s2)        # True (value equality)
print(s1 is s2)        # Implementation-dependent; don't rely on identity for strings

# Bitwise vs logical
print(True & False)    # False (bitwise works on bools but is NOT the logical operator you want)
print(True and False)  # False (correct logical operator)

# Prefer parentheses for clarity
x = 3
print((x > 0 and x < 5) or (x == 10))  # True
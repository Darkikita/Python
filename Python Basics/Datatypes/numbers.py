##########################################################################################
# Number Types --------------------------
##########################################################################################
print("Number Types")

# Integers (int)
x = 42
y = -7
z = 10_000  # underscores for readability

# Floating point numbers (float)
pi = 3.14
small = -0.001
exp = 1.0e6  # scientific notation

# Complex numbers (complex)
c1 = 2 + 3j
c2 = complex(5, -2)


##########################################################################################
# Basic Operations --------------------------
##########################################################################################
print("Basic Operations")
a, b = 7, 3

print(a + b)  # Addition → 10
print(a - b)  # Subtraction → 4
print(a * b)  # Multiplication → 21
print(a / b)  # Division (float) → 2.333...
print(a // b)  # Floor division → 2
print(a % b)  # Modulo (remainder) → 1
print(a**b)  # Exponentiation → 343


##########################################################################################
# Built-in Functions --------------------------
##########################################################################################
print("Built-in Functions")

# Arithmetic helpers
print(abs(-5))  # 5
print(round(3.14159, 2))  # 3.14
print(pow(2, 5))  # 32
print(pow(2, 5, 7))  # 4
print(divmod(7, 3))  # (2, 1)
print(min(3, 7, -2))  # -2
print(max(3, 7, -2))  # 7
print(sum([1, 2, 3]))  # 6

# Type conversions
print(int(3.9))  # 3
print(float(7))  # 7.0
print(complex(2, 3))  # (2+3j)

# Numeric base conversions
print(bin(10))  # '0b1010'
print(oct(10))  # '0o12'
print(hex(10))  # '0xa'

# Character ↔ Unicode conversions
print(ord("A"))  # 65
print(chr(65))  # 'A'

# Type checks
print(isinstance(5, int))  # True
print(isinstance(3.14, float))  # True


##########################################################################################
# Extended Modules --------------------------
##########################################################################################
print("Extended Modules")

# math module (mathematical functions)
import math

print(math.sqrt(16))  # 4.0
print(math.log(100, 10))  # 2.0
print(math.sin(math.pi / 2))  # 1.0

# decimal module (exact decimal arithmetic)
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))  # 0.3 (exact, unlike float)

# fractions module (fractions with numerator/denominator)
from fractions import Fraction

print(Fraction(3, 4) + Fraction(1, 4))  # 1

# random module (random numbers)
import random

print(random.randint(1, 6))  # random int between 1 and 6
print(random.choice(["a", "b", "c"]))  # random element

# statistics module (statistical functions)
import statistics

data = [1, 2, 2, 3, 4]
print(statistics.mean(data))  # 2.4
print(statistics.median(data))  # 2
print(statistics.stdev(data))  # 1.140...

# cmath module (complex math)
import cmath

print(cmath.sqrt(-1))  # 1j

# numbers module (abstract base classes for numbers)
import numbers

print(isinstance(5, numbers.Integral))  # True
print(isinstance(3.14, numbers.Real))  # True

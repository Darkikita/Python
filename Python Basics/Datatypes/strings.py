##########################################################################################
# Strings --------------------------
##########################################################################################
print("Strings")

# Basic strings
s1 = "Hello"
s2 = "World"
s3 = """This is
a multi-line
string."""
print(s1, s2, s3)


##########################################################################################
# Escape Sequences --------------------------
##########################################################################################
print("Escape Sequences")
# \n   = newline (line break)
print("Line break:\nSecond line")
# \t   = tab
print("Tab:\tIndented")
# \\   = backslash
print("Backslash: \\")
# \"   = double quote
# \'   = single quote
print("Quote: \"double\" and 'single'")
# \r   = carriage return
# \b   = backspace
# \f   = form feed
# \uXXXX = Unicode character (e.g. "\u03A9" → Ω)
# \UXXXXXXXX = Unicode (32-bit)
# \N{name} = Unicode by name (e.g. "\N{GREEK CAPITAL LETTER OMEGA}" → Ω)


##########################################################################################
# Formatted strings (f-strings) --------------------------
##########################################################################################
name = "Alice"
age = 30
print(f"My name is {name}, I am {age} years old.")
print(f"{2 + 3=}")  # expression inside f-string → 2 + 3=5

# Old-style formatting
print("Name: %s, Age: %d" % (name, age))

# str.format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))


##########################################################################################
# String Methods --------------------------
##########################################################################################
print("String Methods")

txt = "  Python is Great!  "

# len
print(len(txt))  # 19 (length of string)

# Case methods
print(txt.upper())  # "  PYTHON IS GREAT!  "
print(txt.lower())  # "  python is great!  "
print(txt.title())  # "  Python Is Great!  "
print(txt.capitalize())  # "  python is great!  "

# Trimming whitespace
print(txt.strip())  # "Python is Great!"      -> entfernt Leerzeichen auf beiden Seiten
print(
    txt.rstrip()
)  # "  Python is Great!"   -> entfernt die Leerzeichen rechts (am Ende)
print(
    txt.lstrip()
)  # "Python is Great!  "   -> entfernt die Leerzeichen links (am Anfang)

# Search & replace
print("x" in txt)  # False
print("Python" in txt)  # True
print(txt.find("P"))  # returns index 3
print(txt.find("Great"))  # returns index 11
print(txt.find("x"))  # doesnt exist in the String (-1)
print(txt.replace("Great", "Awesome"))  # "  Python is Awesome!  "

# Check content
print("123".isdigit())  # True
print("abc".isalpha())  # True
print("abc123".isalnum())  # True
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))  # True

# Splitting and joining
words = txt.split()  # ['Python', 'is', 'Great!']
print(words)
print("-".join(words))  # Python-is-Great!


##########################################################################################
# External String Helpers --------------------------
##########################################################################################
print("External String Helpers")

import textwrap

long_text = "Python is a powerful programming language that lets you work quickly and integrate systems more effectively."
print(textwrap.fill(long_text, width=30))  # wraps text to 30 chars per line

import string

print(string.ascii_letters)  # abcdefghijkl...XYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[]^_`{|}~

import re

pattern = r"\d+"
print(re.findall(pattern, "Order 123, item 456"))  # ['123', '456']


##########################################################################################
# Special String Tricks --------------------------
##########################################################################################
print("Special String Tricks")

# Repetition
print("ha" * 3)  # "hahaha"

# Slicing
text = "Python"
print(text[0])  # P
print(text[-1])  # n
print(text[0:3])  # Pyt
print(text[::-1])  # nohtyP (reverse string)

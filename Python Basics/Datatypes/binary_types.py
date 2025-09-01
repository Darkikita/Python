##########################################################################################
# Binary Types --------------------------
##########################################################################################
# -----------------------------------------------------------------
# Binary types in Python:
# bytes        → immutable sequence of bytes (values 0–255)
# bytearray    → mutable sequence of bytes (can be modified in place)
# memoryview   → view object exposing memory of another binary object (bytes, bytearray)
# -----------------------------------------------------------------
# Properties:
# - store raw binary data (useful for files, network, cryptography)
# - elements are integers (0–255)
# - support indexing, slicing, iteration
# - bytes are immutable, bytearray mutable
# - memoryview avoids copying data, allows efficient slicing
# -----------------------------------------------------------------
# Common methods:
# bytes/bytearray:
#   decode(encoding)   → convert to string
#   hex()              → return hex representation
#   fromhex(str)       → create bytes from hex string
#   count(x)           → count occurrences of byte value
#   find(sub)          → find subsequence
# memoryview:
#   tolist()           → convert to list of integers
#   cast(fmt)          → view memory with different format
# -----------------------------------------------------------------
print("Binary Types")

##########################################################################################
# Bytes (immutable)
##########################################################################################
print("Bytes")

b = b"Hello"          # literal with b-prefix
print(b)              # b'Hello'
print(type(b))        # <class 'bytes'>

# indexing and slicing
print(b[0])           # 72 (ASCII of 'H')
print(b[1:4])         # b'ell'

# hex representation
print(b.hex())        # 48656c6c6f
print(bytes.fromhex("48656c6c6f"))  # b'Hello'

# decoding to string
print(b.decode("utf-8"))   # Hello

##########################################################################################
# Bytearray (mutable)
##########################################################################################
print("Bytearray")

ba = bytearray(b"Hello")
print(ba)             # bytearray(b'Hello')

# modify in place
ba[0] = 74            # ASCII 'J'
print(ba)             # bytearray(b'Jello')

# append
ba.append(33)         # '!' (ASCII 33)
print(ba)             # bytearray(b'Jello!')

# slice assignment
ba[1:3] = b"aa"
print(ba)             # bytearray(b'Jaalo!')

##########################################################################################
# Memoryview (efficient view on binary data)
##########################################################################################
print("Memoryview")

data = bytearray(b"Python")
mv = memoryview(data)
print(mv[0])          # 80 (ASCII 'P')

# slice without copy
print(mv[0:3].tobytes())   # b'Pyt'

# modify underlying bytearray through memoryview
mv[0] = 74                 # ASCII 'J'
print(data)                # bytearray(b'Jython')

# convert to list
print(mv.tolist())         # [74, 121, 116, 104, 111, 110]

##########################################################################################
# Common Functions for Binary Types
##########################################################################################
# len(obj) → number of bytes
# bytes(iterable) → create bytes from iterable of ints (0–255)
# bytearray(iterable) → create mutable bytearray
##########################################################################################
print("Common Functions")

print(len(b))                 # 5
print(bytes([65, 66, 67]))    # b'ABC'
print(bytearray([65, 66, 67]))# bytearray(b'ABC')
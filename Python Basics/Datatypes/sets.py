##########################################################################################
# Sets (Unordered Collections of Unique Elements)
##########################################################################################
# -----------------------------------------------------------------
# Set properties:
# - mutable          → can be changed after creation
# - unordered        → no index/position, iteration order is arbitrary
# - unique elements  → duplicates are removed automatically
# - hashable only    → elements must be hashable (e.g., int, str, tuple)
# - fast membership  → "x in s" is on average O(1)
# - not subscriptable→ no indexing/slicing (use loops or set ops)
# -----------------------------------------------------------------
# Common set methods:
# add(x)                  → add single element
# update(iterable, ...)   → add many elements (union in-place)
# remove(x)               → remove x or raise KeyError if missing
# discard(x)              → remove x if present, do nothing otherwise
# pop()                   → remove & return an arbitrary element
# clear()                 → remove all elements
# copy()                  → shallow copy
# union(*others)          → new set with all elements (| operator)
# intersection(*others)   → new set with common elements (& operator)
# difference(*others)     → new set with elements not in others (- op)
# symmetric_difference(t) → new set with elements in either, not both (^)
# issubset(t)             → s ⊆ t  (<= operator)
# issuperset(t)           → s ⊇ t  (>= operator)
# isdisjoint(t)           → True if s and t share no elements
# -----------------------------------------------------------------
print("Sets")

# create sets
a = {1, 2, 3}
b = set([3, 4, 5])  # from iterable
print(a, b)  # {1, 2, 3} {3, 4, 5}

# uniqueness
dup = {1, 1, 2, 2, 3}
print(dup)  # {1, 2, 3}

# membership (fast)
print(2 in a)  # True
print(9 in a)  # False

# add, update
a.add(10)
print(a)  # {1, 2, 3, 10}
a.update([20, 30], {3, 40})
print(a)  # {1, 2, 3, 10, 20, 30, 40}

# remove vs discard
a.discard(999)  # no error
print(a)
# a.remove(999)      # would raise KeyError
a.remove(10)
print(a)

# pop (arbitrary element)
popped = a.pop()
print(popped, a)

# clear/copy
c = a.copy()
c.clear()
print(c)  # set()

##########################################################################################
# Set Operations (return new sets)
##########################################################################################
print("Set Operations")

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

print(x.union(y))  # {1,2,3,4,5,6}
print(x | y)  # same as union
print(x.intersection(y))  # {3,4}
print(x & y)  # same as intersection
print(x.difference(y))  # {1,2}
print(x - y)  # same as difference
print(x.symmetric_difference(y))  # {1,2,5,6}
print(x ^ y)  # same as symmetric_difference

##########################################################################################
# Relations Between Sets
##########################################################################################
print("Set Relations")

s = {1, 2}
t = {1, 2, 3}

print(s.issubset(t))  # True
print(s <= t)  # True  (subset)
print(t.issuperset(s))  # True
print(t >= s)  # True  (superset)
print(s.isdisjoint({9}))  # True  (no overlap)

##########################################################################################
# Frozenset (Immutable Set)
##########################################################################################
# -----------------------------------------------------------------
# Frozenset properties:
# - immutable       → cannot be changed after creation
# - hashable        → can be used as dict keys or set elements
# - supports set ops that return new frozensets (|, &, -, ^)
# -----------------------------------------------------------------
print("Frozenset")

fs = frozenset([1, 2, 3])
print(fs)
# fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
print(fs | frozenset([3, 4]))  # frozenset({1, 2, 3, 4})

##########################################################################################
# Common Functions for Sets
##########################################################################################
# len(set)    → number of elements
# set(iterable) → create set from iterable
# sorted(set) → sorted list of elements (since sets are unordered)
##########################################################################################
print("Common Functions")

s2 = {7, 3, 9, 1}
print(len(s2))  # e.g. 4
print(set("hello"))  # {'h','e','l','o'}
print(sorted(s2))  # [1, 3, 7, 9]

##########################################################################################
# Set Comprehensions
##########################################################################################
print("Set Comprehensions")

nums = [1, 2, 2, 3, 4, 4]
squares = {n * n for n in nums}  # deduplicate & transform
evens = {n for n in range(10) if n % 2 == 0}
print(squares)  # {1, 4, 9, 16}
print(evens)  # {0, 2, 4, 6, 8}

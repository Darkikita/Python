# Data Structures
#   - Filter Function
#   - List Comprehensions
#   - Zip Function
#   - Stacks




#------------------------------------------------------------------------------
# Filter Function

items =[
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
    ("Product4", 30)
]   

filtered = filter(lambda item:item[1] > 15, items)
print(list(filtered))

# item[1] > 15 is a boolean, if true this value will be returned



#------------------------------------------------------------------------------
# List Comprehensions

items =[
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
    ("Product4", 30)
]   

#before
prices = list(map(lambda item: item[1], items)) 
print("prices:", prices)

filtered = list(filter(lambda item:item[1] > 15, items))
print("filtered:", filtered)


#now
# [expression for item in tiems]
prices2 = [item[1] for item in items] 
print("prices2:", list(prices2))


# [expression for item in items if....]
# [item for item in items if...]
filtered2 = [item for item in items if item[1] > 15]
print("filtered2:", list(filtered2))


# just happend, shoes that "item[1] > 15" is a boolean
filtered3 = [item[1] > 15 for item in items]
print("filtered3:", list(filtered3))


# Ausgesprochen

prices = [item[1] for item in items] 
# in die Liste "prices" kommt die zweite Stelle ([1]) des item für (for) jedes item in der Liste "items"


filtered = [item for item in items if item[1] > 15]
# in die Liste "filtered" kommt ein vollständiges item für (for) jedes item in der Liste "items" 
# wenn die Bedinung das die zweite Stelle ([1]) von item größer als 15 (> 15) ist



#------------------------------------------------------------------------------
# Zip Function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

tuple_list = [(1, 10), (2, 20), (3, 30)]
print(tuple_list)

# to achive this we use the build in Zip-Function
tuple_list2 = zip(list1, list2)
print(list(tuple_list2))

# String to zip function
print(list(zip("abc",list1, list2)))


# zip cuttoff
list3 = [100, 200, 300, 400]

print(list(zip("abc",list1, list2, list3)))

print(list(zip("ab",list1, list2, list3)))

#------------------------------------------------------------------------------
# Stacks

#LIFO Last in - First Out (Browser - Back Button)

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
print(browsing_session)

last = browsing_session.pop()   # pop-Method returns the removed item from the stack
print(last)

print(browsing_session)

print("redirect to", browsing_session[-1])



if not browsing_session:        # empty list = false; not empty list = true
    print("disable Backbutton")
else:
    last = browsing_session.pop()
    print("removed: ", last)
    print("redirect to", browsing_session[-1])
    print(browsing_session)






# Classes
#   - Private Members
#   - Properties
#   - 
#   - 
#   - 



#------------------------------------------------------------------------------
# Private Members

class TagCloud:
    
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):                     #allows dictonary access through object[key]
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")


print(cloud.tags["python"])
#print(cloud.tags["PYTHON"]) # KeyError: 'PYTHON'



# We have access to the underlying dictionary via cloud.tags[]
# so we want to hide this attribute from the outside



class TagCloud2:
    
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):                     #allows dictonary access through object[key]
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)


cloud2 = TagCloud2()
cloud2.add("python")
cloud2.add("python")
cloud2.add("python")


# print(cloud2.__tags) # AttributeError: 'TagCloud2' object has no attribute '__tags'

# but its still accessable

print(cloud2.__dict__)

print(cloud2._TagCloud2__tags)

cloud2._TagCloud2__tags["python"] = 5       #manipulation possible

print(cloud2._TagCloud2__tags)



#------------------------------------------------------------------------------
# Properties

class Product:
    def __init__(self, price):
        self.price = price


product = Product(-50)
print(product.price)

# is possible, shouldnt be


# My selftry
class Product2:
    def __init__(self):
        return None

    def getting(self):
        return self.__price
    
    def setting(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("a price cannot be negative")


# product2 = Product2(-50) # irrelevant because __prive is not accessable
# print(product2.__price) #AttributeError: 'Product2' object has no attribute '__price'

product2 = Product2()
product2.setting(40)
print(product2.getting())


#CwM Correct Coding


class Product3:
    def __init__(self, price):
        self.setting(price)             #calling the setting method in the constructor

    def getting(self):
        return self.__price
    
    def setting(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("a price cannot be negative")      # print("a price cannot be negative")  



product3 = Product3(40)
print(product3.getting())

#product30 = Product3(-40)


# this Code is what a Java Programmer would write in Python 
# here is where we use Properties

#Introducing property
class Product4:
    def __init__(self, price):
        self.setting(price)

    def getting(self):
        return self.__price
    
    def setting(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("a price cannot be negative")      # print("a price cannot be negative")  

    price = property(getting, setting)


product4 = Product4(40)
print(product4.price)

product4.price = 100
print(product4.price)

#product4.price = -50  #ValueError: a price cannot be negative


#property decorator
class Product5:
    def __init__(self, price):
        self.price = price              # we change this call with our price-property

    @property                   #always above the getter method
    def price(self):
        return self.__price
    
    @price.setter               #always name of the decorator name of setter method
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("a price cannot be negative")      # print("a price cannot be negative")  




product5 = Product5(40)
print(product5.price)

product5.price = 100
print(product5.price)



#creating a class without a setter, so only a initialisation value can be passed
class Product6:
    def __init__(self, price):
        self.__price = price              

    @property                  
    def price(self):
        return self.__price
    
    # @price.setter              
    # def price(self, value):
    #     if value >= 0:
    #         self.__price = value
    #     else:
    #         raise ValueError("a price cannot be negative")     




product6 = Product6(40)
print(product6.price)

#product6.price = 50 #AttributeError: property 'price' of 'Product6' object has no setter

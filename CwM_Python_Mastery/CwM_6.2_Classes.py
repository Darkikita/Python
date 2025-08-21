# Classes
#   - Comparing Objects
#   - Performing Arithmetic Operations
#   - Making Custom Containers
#   - Selbstexperiment





#------------------------------------------------------------------------------
# Comparing Objects


class Point:  

    def __init__(self, x, y):              
        self.x = x
        self.y = y


point = Point(2,3)
other = Point(2,3)
print(point == other)   #False: References/Adresses are compared 
print(point.__eq__(other))  # NotImplemented



# Comparison Magic Methodes
# we create __eq__
print("Point2")

class Point2:  

    def __init__(self, x, y):              
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point2 = Point2(2,3)
other2 = Point2(2,3)
print(point2 == other2)   #True: Magic Method 
print(point2.__eq__(other2))     #True

# print(point2 > other2)  #TypeError: '>' not supported between instances of 'Point2' and 'Point2'


# Comparison Magic Methodes
# we create __gt__
print("Point3")


class Point3:  

    def __init__(self, x, y):              
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x or self.y > other.y


point3 = Point3(2,4)
other3 = Point3(2,3)

print(point3 > other3)  # True
print(point3 < other3)  # __lt__ didnt have to be implemented



#------------------------------------------------------------------------------
# Performing Arithmetic Operations

class Point4:  

    def __init__(self, x, y):              
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point4(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point4 = Point4(10,20)
other4 = Point4(1,2)
#print(point4 + other4)  #TypeError: unsupported operand type(s) for +: 'Point4' and 'Point4'
another4 = point4.__add__(other4)
another4.draw()


#------------------------------------------------------------------------------
# Making Custom Containers

# Common Datastructures List, Dictonaries, Sets... are Containertypes

# Own custom Containertype TagCloud: 
# keep track of the number of various tags of a block

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
cloud.add("java")
cloud.add("Python")

print(cloud.tags)

print(cloud["python"])
print(cloud["javascript"])
print(cloud["Python"])
cloud["python"] = 10
print(cloud["Python"])

print(cloud.tags)
print(len(cloud))

for item in cloud:
    print(item)

# len(cloud)
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)



#------------------------------------------------------------------------------
# Selbstexperiment


class TagCloud2:
    
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def ausgabe(self):
        for key, value in self.tags.items():
            print(f"Key: {key}, Value: {value}")

    def ausgabe2(self):
        for key in self.tags:
            print(f"Key: {key}")

    def ausgabe3(self):
        for key in self.tags:
            print(f"Key: {key}, Value: {self.tags.get(key)}")

    def ausgabe4(self):
        for key, value in self.tags.items():
            yield key, value  # Gibt Tupel (Key, Value) zurück

    def ausgabe5(self):
        for key in self.tags:
            yield key, self.tags.get(key) 

    def ausgabe6(self):
        for key in self.tags:
            yield key, self.tags.get(key) 


    def items_selfmade(self):               # so funktioniert items()
        for key in self.tags:
            yield key, self.tags[key]  # Gibt Tupel (Key, Value) zurück



cloud2 = TagCloud2()
cloud2.add("python")
cloud2.add("python")
cloud2.add("python")
cloud2.add("java")
cloud2.add("Python")

print(cloud2.tags)

cloud2.ausgabe()
cloud2.ausgabe2()
cloud2.ausgabe3()
print(list(cloud2.ausgabe4()))
print(list(cloud2.ausgabe5()))
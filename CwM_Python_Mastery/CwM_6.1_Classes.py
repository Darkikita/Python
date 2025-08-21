# Classes
#   - Classes
#   - Creating Classes
#   - Constructors
#   - Class vs Instance Attributes
#   - Class vs Instance Methods
#   - Magic Methods



#------------------------------------------------------------------------------
# Classes

numbers = [1, 2]
numbers.append #Method

x = 1
print(type(x))

# Class is a blueprint for creating new objects
# Object is an instance of a class

# Class: Human
#Objects: John, Mary, Jack



#------------------------------------------------------------------------------
# Creating Classes

class Point:                     #Pascal naming convention: MyPointIsThis
    def draw(self):
        print("draw")



point = Point()
point.__dict__                  # This class has his Methods from another Class in Python through inhearatance
print(type(point))              # <class '__main__.Point'> ; __main__ is the name of our Module
print(isinstance(point, Point))        # is this object ("point") an instance of a given Class "Point"
print(isinstance(point, int))  


#------------------------------------------------------------------------------
# Constructors

#Self is a reference to the current point object

class Point2:  
    def __init__(self, x, y):                 #Magic Method which is a constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")



point2 = Point2(1, 2)
print(point2.x)
point2.draw()


#------------------------------------------------------------------------------
# Class vs Instance Attributes


class Point3:  
    default_color = "red"

    def __init__(self, x, y):                 #Magic Method which is a constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y}) & Color: {self.default_color}")



point3 = Point3(1, 2)
point3.z = 10
point3.draw()
print(point3.z)


another3 = Point3(3, 4)
another3.draw()

print("Changing the attribute")

point3.default_color = "green"   # Es wird eine Instanzvariable erstellt die die Klassenvariable mit dem selben Namen überschreibt
point3.draw()
another3.draw()

Point3.default_color = "yellow"
point3.draw()            # point besitzt bereits eine Instanzvariable
another3.draw()          # another greift weiterhin auf die Klassenvariable zu


#------------------------------------------------------------------------------
# Class vs Instance Methods


class Point4:  

    def __init__(self, x, y):                
        self.x = x
        self.y = y

    @classmethod            # decorator
    def zero(cls):          #whenever we creat a class Method, by convention it first parameter is cls
        return cls(0,0)     # same a creating Point-Object and giving it the attributes (0,0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")



point4 = Point4.zero()    #Factory Method, it creates an Object itself
point4.draw()


#------------------------------------------------------------------------------
# Magic Methods


class Point5:  

    def __init__(self, x, y):              
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point5 = Point5(1,2)
print(point5)       # <__main__.Point5 object at 0x000002955942EB90>
print(Point5)       # <class '__main__.Point5'>
point5.__str__      # Out Class inherted Methods from another Class
print(point5.__str__ )

# Now we will reimplement the __str__ Method


class Point6:  

    def __init__(self, x, y):              
        self.x = x
        self.y = y

    def __str__(self):
        return f"this is out reimplemented method that returns: ({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")



point6 = Point6(2, 3)
print(point6)
print(str(point6))



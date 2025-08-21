# Classes
#   - Inheritance
#   - The Object Class
#   - Method Overriding
#   - Multi-level Inheratance
#   - Multiple Inheritance


#------------------------------------------------------------------------------
# Inheritance

class Animal:           # Parent, Base
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):   # Child, Sub
    def __init__(self):
        super().__init__()      #also can be called after the Mammal Constructor
        self.weight = 100
    
    def walk(self):
        print("walk")


class Fish(Animal):      # Child, Sub
    def swim(self):
        print("swim")


tiger = Mammal()
tiger.eat()
print(tiger.age)



#------------------------------------------------------------------------------
# The Object Class

#usefull built in functions

print(isinstance(tiger, Mammal))
print(isinstance(tiger, Animal))

print(isinstance(tiger, object))    

thing = object()
thing.__dir__   #all those magic methodes are from the class object

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))


#------------------------------------------------------------------------------
# Method Overriding

#without super()
#print(tiger.age)    #AttributeError: 'Mammal' object has no attribute 'age'
print(tiger.weight) 

# the constructor of child: Mammal overrid the constructor of parent: Animal
# -> this is called: Method Overriding


#with super()
print(tiger.age)    #AttributeError: 'Mammal' object has no attribute 'age'
print(tiger.weight) 




#------------------------------------------------------------------------------
# Multi-level Inheratance

class Animal:      
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass            # every class needs at least one statement

#Problem: Chicken cannot fly

# Multilevel Inheritance should be avoided at all times



#------------------------------------------------------------------------------
# Multiple Inheritance


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()     #Employee Greet

# the first Inherited Class will override the other class with homonymity of methods


# Good Example

class Flyer:
    def fly(self):
        print("fly")


class Swimmer:
    def swimm(self):
        print("swimm")


class FlyingFish(Flyer, Swimmer):
    pass


flyfish = FlyingFish()
flyfish.swimm()
flyfish.fly()


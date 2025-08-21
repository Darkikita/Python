# Classes
#   - Good Example of Inheritance
#   - Abstract Base Classes
#   - Polymorphism
#   - DuckTyping
#   - Extending built-in Types


#------------------------------------------------------------------------------
# Good Example of Inheritance
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):      #AbstractBaseClass
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")



#------------------------------------------------------------------------------
# Abstract Base Classes

# Before import ABC 
# stream = Stream()   #1. shouldnt be able to do this
# stream.open()

# 2. in case we implement a new subclass, we should have a common interface



class MemoryStream(Stream):
    pass

#memory_stream = MemoryStream() 
# TypeError: Can't instantiate abstract class MemoryStream with abstract method read



class MemoryStreamCorrect(Stream):
    def read(self):
        print("Reading data from a memory")

memory_stream2 = MemoryStreamCorrect() 
memory_stream2.read()




#------------------------------------------------------------------------------
# Polymorphism

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    control.draw()


ddl = DropDownList()
print(isinstance(ddl, UIControl))
draw(ddl)

tb = TextBox()
draw(tb)


def draw2(controls):
    for control in controls:
        control.draw()

draw2([ddl, tb])



#------------------------------------------------------------------------------
# DuckTyping


def draw2(controls):
    for control in controls:
        control.draw()

#Python does not need the UIControll Class at all, this method can be used anywhere, as long as controls
# is an itterable that is passed and control has a draw() Method
# if it walks like a duck and talks like a duck its is a duck 



#------------------------------------------------------------------------------
# Extending built-in Types

#Selbstversuch
class Text_nd(str):

    def duplicate(self, text):
        self.text = text * 2
        return self.text
    

test_nd = Text_nd()
print(test_nd.duplicate("Hallo"))
print(test_nd.duplicate("Hallo").lower())       #Mulitple method call, only if the first method return smt to the second
#---


class Text(str):

    def duplicate(self):
        return self + self


test = Text("Python")
print(test)
print(test.lower())         # has all methodes from str
print(test.duplicate())
print(test.duplicate().lower())



#Selbstversuch
class List(list):

    def __init__(self):
        super().__init__()

    def append(self, list_object):
       return self[:] + list_object         #self[:]

list_sp = ["bla", 1]
list_obj = List()
print(list_obj.append(list_sp))
#----


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)



test_list = TrackableList()
test_list.append("bla")

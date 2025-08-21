##########################################################################################
# Type System --------------------------
##########################################################################################
print("Type System")

# type() - get the type of an object
a = 4.0
print(type(a))  # <class 'float'>

b = "Hello"
print(type(b))  # <class 'str'>


# isinstance() - check if object is instance of a class (or tuple of classes)
x = 5
print(isinstance(x, int))  # True
print(isinstance(x, (float, int)))  # True (since x is int, and tuple contains int)
print(isinstance(b, str))  # True
print(isinstance(b, list))  # False


# issubclass() - check if class is subclass of another class
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False


# callable() - check if object can be called like a function
def my_func():
    return "hi"


print(callable(my_func))  # True
print(callable(42))  # False


# id() - get unique identifier (memory address) of object
print(id(a))


##########################################################################################
# Typing hints (type annotations) --------------------------
##########################################################################################
print("Typing Hints")


# Function annotations
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."


print(greet("Alice", 30))

# Variable annotations
count: int = 10
price: float = 19.99

##########################################################################################
# Typing Module  --------------------------
##########################################################################################
from typing import List, Dict, Tuple, Set, Union, Optional, Any

# Variable annotations
name: str = "Alice"
age: int = 30
scores: List[int] = [100, 90, 80]
config: Dict[str, str] = {"host": "localhost", "port": "8080"}
person: Tuple[str, int] = ("Charlie", 40)
values: Set[float] = {1.1, 2.2, 3.3}


# Function annotations
def greet2(user: str, active: bool) -> str:
    return f"Hello {user}, active={active}"


# Union → kann mehrere Typen sein
def square(x: Union[int, float]) -> float:
    return x * x


# Optional → entweder Typ oder None
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None


# Any → beliebiger Typ erlaubt
def log_data(data: Any) -> None:
    print("Logging:", data)

Python-OOPS Notes

What is an abstract class? 
What is an interface?

An abstract class is a way in python to describe
the basic methods that the implementing class 
should implement.

An abstract class can have both concrete and abstract methods
Concrete methods are implemented in abstract class
while abstract methods have no implementation.

Any inherited class that inherits the abstract class
will have to implement the abstract methods 
and MAY override the concrete method of the abstract class if needed

====

from abc import ABC, abstractmethod
class Shape(ABC):
    def draw(self): #concrete method
        print("drawing shape")
    @abstractmethod
    def area(self): #abstract method
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def draw(self):
        print("drawing rectangle")

======

n this example, Shape is an abstract class with a 
concrete method draw and an abstract method area.
Rectangle is a class that inherits from the Shape class 
and overrides the draw method to provide a different 
implementation.

======

Interfaces in Python are a very similar concept
but in interfaces you can't have any concrete methods
You always have to have abstract methods.

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

====
It's worth noting that, when a class implements an interface,
it must implement all the abstract methods defined in that 
interface. If a class does not implement all the methods,
 it will result in a TypeError.
====
Also for the inherited class inheriting the abstract class as well 
it will have to implement all the abstract methods
It won't throw an error like in interface 
but it will again be an abstract class
====



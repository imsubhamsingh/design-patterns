# Factory Method is a creational design pattern that provides an interface
# for creating objects in a superclass, but allows subclasses 
# to alter the type of objects that will be created.

# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Factory Concept"
from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    "An abstract class product interface"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"
        pass


class ConcreateProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"
    
    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"
    
    def create_object(self):
        return self


class Creator:
    "The Factory class"
    
    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == "A":
            return ConcreateProductA()
        if some_property == "B":
            return ConcreteProductB()
        if some_property == "C":
            return ConcreteProductC()

# Client 
PRODUCT = Creator.create_object("B")
print(PRODUCT.name)

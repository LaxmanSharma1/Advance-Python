
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        pass

class ProductA(IProduct): 

    def __init__(self) -> None:
        self.name = 'A'
    
    def create_object(self):
        return self
    
class ProductB(IProduct): 

    def __init__(self) -> None:
        self.name = 'B'

    def create_object(self):
        return self
    
class ProductC(IProduct): 

    def __init__(self) -> None:
        self.name = 'C'

    def create_object(self): 
        return self
    
class FactoryA:

    @staticmethod
    def create_object(name):
        if name == 'a':
            return ProductA()
        elif name == 'b': 
            return ProductB()
        elif name == 'c':
            return ProductC()
        else:
            return None

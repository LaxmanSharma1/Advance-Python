
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        pass

class ProductX(IProduct): 

    def __init__(self) -> None:
        self.name = 'X'
    
    def create_object(self):
        return self
    
class ProductY(IProduct): 

    def __init__(self) -> None:
        self.name = 'Y'

    def create_object(self):
        return self
    
class ProductZ(IProduct): 

    def __init__(self) -> None:
        self.name = 'Z'

    def create_object(self): 
        return self
    
class FactoryB:

    @staticmethod
    def create_object(name):
        if name == 'x':
            return ProductX()
        elif name == 'y': 
            return ProductY()
        elif name == 'z':
            return ProductZ()
        else:
            return None


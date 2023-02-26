from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    """
    Interface for a hypothetical product interface
    """

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract method"
    


class ProductA(IProduct):

    def __init__(self, name:str) -> None:
        self.name = name
    
    def create_object(self):
        return self

class ProductB(IProduct): 

    def __init__(self, name:str) -> None:
        self.name = name

    def create_object(self): 
        return self
    
class ProductC(IProduct): 

    def __init__(self, name:str) -> None:
        self.name = name

    def create_object(self):
        return self
    
class Creator:
    """
    The Factory Class
    """

    @staticmethod
    def create_object(typeOfProduct, nameOfProduct):
        if(typeOfProduct == "A"): 
            return ProductA(nameOfProduct)
        elif(typeOfProduct == "B"):
            return ProductB(nameOfProduct)
        elif(typeOfProduct == "C"):
            return ProductC(nameOfProduct)
        else:
            return None
        

product = Creator.create_object("A","Product A")

print(product.name)


        
    







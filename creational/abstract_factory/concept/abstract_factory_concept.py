
from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB

class IAbstractFactory(metaclass=ABCMeta): 

    @staticmethod
    @abstractmethod
    def create_object(factory,name):
        pass

class AbstractFactory(IAbstractFactory): 

    @staticmethod
    def create_object(factory,name):
        if factory == 'a':
            return FactoryA.create_object(name)
        elif factory == 'b':
            return FactoryB.create_object(name)
        else:
            return None
    

# client
def main():
    factory = input("Enter the factory name you want to create object from: ")
    name = input("Enter the name of product that you want to create from: ")
    
    product = AbstractFactory.create_object(factory,name)

    if product == None:
        print("Factory or product name is wrong")
    else:
        print(product.name)


if __name__ == "__main__":
    main()
        
    
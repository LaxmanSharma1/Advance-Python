import copy

class Singleton(): 
    
    value = ["this","is","the","singleton","class","instance","variable"]
    def __new__(cls):
        return cls
    
    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls): 
        print(cls.value)

print(f"id(singleton)\t{id(Singleton)}")

object1 = Singleton() 
print(f"id(object1)\t{id(object1)}")

object2 = copy.deepcopy(object1)
print(f"id(object2)\t{id(object2)}")

object3 = Singleton()
print(f"id(object3)\t{id(object3)}")

object1.class_method()
object2.class_method()
object3.class_method()


    

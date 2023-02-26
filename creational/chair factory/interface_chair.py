
from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
    """
    Chair Interface
    """

    @staticmethod
    @abstractmethod
    def get_dimensions():
        pass
        

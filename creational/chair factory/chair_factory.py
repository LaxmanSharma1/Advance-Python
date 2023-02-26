
from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:

    @staticmethod
    def get_chair(chair):
        if chair == "small":
            return SmallChair()
        elif chair == "medium":
            return MediumChair()
        elif chair == "big":
            return BigChair()
        else:
            return None
    

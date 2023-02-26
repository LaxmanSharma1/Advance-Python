
from chair_factory import ChairFactory

def main():
    chair = input("Enter the type of chair you want ")
    chair = ChairFactory.get_chair(chair)
    if chair is not None: 
        print("Dimensions of the chair are : ", chair.get_dimensions())
    else: 
        print("There is no such type of chair")

if __name__ == "__main__":
    main()
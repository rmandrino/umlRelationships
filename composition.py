# Part class
class Room:
    def display(self):
        print("Room belongs to House")


# Whole class
class House:
    def __init__(self):
        self.room = Room()

    def show_house(self):
        self.room.display()


# Main program
house = House()
house.show_house()
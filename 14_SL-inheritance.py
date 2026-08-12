class Car:
    colour = "black"
    @staticmethod
    def start():
        print("Car started . .")

    @staticmethod
    def stop():
        print("Car stopped . . ")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

# print(car1.name)
print(car1.start())
print(car1.colour)

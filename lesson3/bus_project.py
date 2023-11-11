class Human:
    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passenger = []

    def add_pasenger(self,human):
        self.passenger.append(human)

    def print_passengers_names(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passenger: ")

            for passenger in self.passenger:
                print(passenger.name)

        else:
            print(f"There are no passengers in {self.brand}")


nazar = Human("Nazar")
mary = Human("Mary")

car = Auto("BMW")

car.add_pasenger(nazar)
car.add_pasenger(mary)
car.print_passengers_names()






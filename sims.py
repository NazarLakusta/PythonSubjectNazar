from random import *
class Human:
    def __init__(self,name,job=None,home=None,car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.gladness = 50
        self.satiety = 50
        self.money = 100

    def get_home(self):
        self.home = House

    def get_car(self):
        self.car = Auto()



class Auto:

    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.fuel = brand_list[self.brand]["fuel"]

    def drive(self):
        if self.strength>0 and  self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


brands_of_car = {
 "BMW":{"fuel":100, "strength":100, "consumption":6},
 "Lada":{"fuel":50, "strength":40, "consumption":10},
 "Ferrari":{"fuel":80, "strength":120, "consumption":14},

}
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0



class Job:

    def __init__(self,job_list):
        self.job = 0
        self.salary = 0
        self.gladness = 0



job_list = {
    "Java developer":{"salary":50, "gladness_less":10},
    "Python developer":{"salary":40, "gladness_less":3},
    "Photoshop designer":{"salary":45,"gladness_less":25}
}
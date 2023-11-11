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
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass

        else:
            self.to_repair()
            return

        self.job = Job(job_list)


    def eat(self):
       if self.home.food <=0:
           self.shopping("food")

       else:
            if self.satiety >100:
                self.satiety = 100
                return

            self.satiety +=5
            self.home.food -= 5


    def work(self):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4


    def shopping(self,message):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                message = "fuel"
                return
            else:
                self.to_repair()
                return

        if message == "fuel":
            print("I bought fuel")
            self.money -=100
            self.car.fuel += 100

        elif message == "food":
            print("I bought food")
            self.money-=50
            self.home.food += 50

        elif message == "delicacies":
            print("Hooraaay!! Delicious!")
            self.gladness += 10
            self.satiety +=2
            self.money-=15


        # ви купили delicacies    ,  збільшити радість, ситість, зменшити гроші

    def chill(self):
        self.gladness+=10
        self.home.mess+=5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self,day):
        print(f"day: {day}")

        print()

        print("==="*20)
        print(f"Human: {self.name}")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")
        print("===" * 20)

        print()

        print("///" * 20)
        print("Info about house:")
        print(f"Food: {self.home.food}")
        print(f"Mess: {self.home.mess}")
        print("///" * 20)

        print()

        print("***"*20)
        print("Info about Car")
        print(f"Brand: {self.car.brand}")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")



    def is_alive(self):
        if self.money < -500 :
            print("Bankrupt..")
            return False

        if self.gladness<0:
            print("Depression...")
            return False

        if self.satiety:
            print("Dead..")
            return False




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
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness = job_list[self.job]["gladness_less"]



job_list = {
    "Java developer":{"salary":50, "gladness_less":10},
    "Python developer":{"salary":40, "gladness_less":3},
    "Photoshop designer":{"salary":45,"gladness_less":25}
}
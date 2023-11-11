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
       if self.home.food <= 0:
           self.shopping("food")

       else:
            if self.satiety > 100:
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

        if self.satiety<0:
            print("Dead..")
            return False

    def live(self,day):
        if self.is_alive() == False:
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(f" I don't have a job, goint to get a job {self.job.job}"
                  f" with salary {self.job.salary}")

        self.days_indexes(day)

        dice = randint(1,4)

        if self.satiety < 20:
            print("I'll go eat")
            self.eat()

        elif self.gladness < 20:
            if self.home.mess>15:
                print("I want to chill, but there is so much mess")
                self.clean_home()
            else:
                print("Let's CHill!!")
                self.chill()

        elif self.money < 0:
            print("Start working!")
            self.work()

        elif self.car.strength < 15:
            print("I need to repati my car")
            self.to_repair()

        elif dice == 1:
            print("Let's CHill!!")
            self.chill()

        elif dice == 2:
            print("Start working!")
            self.work()

        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()

        elif dice == 4:
            print("Time for treats!")
            self.shopping(message="delicacies")

brands_of_car = {
 "BMW":{"fuel":100, "strength":100, "consumption":6},
 "Lada":{"fuel":50, "strength":40, "consumption":10},
 "Ferrari":{"fuel":80, "strength":120, "consumption":14},

}
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



class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "Java developer":{"salary":50, "gladness_less":10},
    "Python developer":{"salary":40, "gladness_less":3},
    "Photoshop designer":{"salary":45,"gladness_less":25}
}
class Job:

    def __init__(self,job_list):
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness = job_list[self.job]["gladness_less"]






nazar = Human("Nazar")

for day in range(1,8):
    if nazar.live(day) == False:
        break
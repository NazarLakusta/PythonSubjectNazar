from random import *
class human:
    def __init__(self,name,job=None,car=None,home=None):
        self.money = 10000
        self.name = name
        self.happiness = 60
        self.nohunger = 80
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

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
        if self.house.food <= 0:
            self.shopping("Еда")

        else:
            if self.nohunger >100:
                self.nohunger = 100
                return

            self.nohunger += 5
            self.house.food -= 5

    def work(self):
        if self.car.drive():
            pass

        else:
            if self.car.oil < 20:
                self.shopping("Топливо")
                return
            else:
                self.to_repair()
                return

        self.money += self.job.salary
        self.happiness -= self.job.happiness

    def shopping(self,message):
        if self.car.drive():
            pass

        else:
            if self.car.oil < 20:
                message = ("Топливо")
                return
            else:
                self.to_repair()
                return

        if message == "Топливо":
            print("Я купил топливо")
            self.money -= 100
            self.car.oil += 100
        elif message == "Еда":
            print("Я купил еды")
            self.money -= 50
            self.home.food += 50
        elif message == "Вкусняшки":
            self.money -= 20
            self.home.food += 20
            self.happiness += 20

    def chill(self):
        self.happiness += 10
        self.home.cleaness -= 5

    def clean_home(self):
        self.happiness -= 5
        self.home.cleaness = 0

    def to_repair(self):
        self.car.strong += 100
        self.money -= 50

    def days_indexes(self,day):
        print(f"День: {day}")

        print()

        print("==="*20)
        print(f"Имя: {self.name}")
        print(f"Деньги: {self.money}")
        print(f"Радость: {self.happiness}")
        print(f"Сытость: {self.nohunger}")

        print()

        print("///"*20)
        print("Информация про дом:")
        print(f"Еда: {self.home.food}")
        print(f"Чистота: {self.home.cleaness}")

        print()

        print("***"*20)
        print("Информация про машину:")
        print(f"Бренд: {self.car.brand}")
        print(f"Топливо: {self.car.oil}")
        print(f"Cила: {self.car.strong}")

    def is_alive(self):
        if self.money <= 500:
            print("Вы банкрот!")
            return False
        elif self.nohunger <= 0:
            print("Вы слишком голодны!")
            return False
        elif self.happiness <= 0:
            print("У вас депрессия!")
            return False

    def life(self,day):
        if self.is_alive() == False:
            return False

        if self.home is None:
            print("Вы заселились")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"Я купил машину {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(f"У меня нет работы, пойду работать {self.job.job} с зарплатой {self.job.salary}")

        self.days_indexes(day)

        dice = int(input("Что вы хотите сегодня сделать?"
                   "\n1 - отдохнуть"
                   "\n2 - поработать"
                   "\n3 - убраться"
                   "\n4 - пообедать: "))

        if self.nohunger < 20:
            print("Пойду поем")
            self.eat()

        elif self.happiness <20:
            if self.home.cleaness < 15:
                print("Я хочу отдохнуть, но тут так грязно")
                self.clean_home()
            else:
                print("Пора отдыхать!")
                self.chill()

        elif self.money < 0:
            print("Пора работать!")
            self.work()

        elif self.car.strong < 15:
            print("Я должен починить свою машину!")
            self.to_repair()

        elif dice == 1:
            print("Пора отдыхать!")
            self.chill()

        elif dice == 2:
            print("Пора работать!!")
            self.work()

        elif dice == 3:
            print("Время уборки!")
            self.clean_home()

        elif dice == 4:
            print("Пора обедать!")
            self.shopping(message="Вкусняшки")

class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
        self.oil = brand_list[self.brand]["Топливо"]
        self.strong = brand_list[self.brand]["Сила"]
        self.roshod = brand_list[self.brand]["Расход"]

    def drive(self):
        if self.strong>0 and self.oil > self.roshod:
            self.oil -=  self.roshod
            self.strong -= 1
            return True
        else:
            print("Машина не может ехать дальше")
            return False

brands_of_car = {
    "BMW":{"Топливо":100, "Сила": 100, "Расход": 6},
    "Ferrari":{"Топливо":80, "Сила": 120, "Расход": 14},
    "Lada":{"Топливо":50, "Сила": 40, "Расход": 10}

}



class House:
    def __init__(self):
        self.food = 100
        self.cleaness = 100

class Job:

    def __init__(self,job_list):
        self.job = choice(list(job_list))
        self.happiness = job_list[self.job]["-Счастье"]
        self.salary = job_list[self.job]["Зарплата "]

job_list = {
    "Разработчик Java":{"Зарплата ":50, "-Счастье":10},
    "Разработчик Python":{"Зарплата ":40, "-Счастье":3},
    "Photoshop дизайнер":{"Зарплата ":45, "-Счастье":25}
}

max = human("Max")

for day in range(1,8):
    if max.life(day) == False:
        break
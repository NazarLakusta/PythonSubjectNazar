from random import *
class Student:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.gladness -= 5
        self.progress += 0.12

    def to_sleep(self):
        print("Sleeping...")
        self.gladness += 3

    def to_chill(self):
        print("REEEEESSSSSSSSTTTTTTTT!!!!!!!")
        self.gladness += 5
        self.progress -= 0.1

    def end_of_day(self):
        print("==== Congratulate , day is done ==== \n")

        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")


    def is_alive(self):

        if self.progress < -0.5:
            print("Cast out... ;(")
            self.alive = False

        elif self.gladness < 0:
            print("Depression ;(")
            self.alive = False

        elif self.progress > 5:
            print("YOU WIN!!")
            self.alive = False


    def live(self,day):

        print()
        print("=="*20)
        print("Day number is: ",day)

        live_random = randint(1,3)

        if live_random == 1:
            self.to_study()

        elif live_random == 2:
            self.to_chill()

        elif live_random == 3:
            self.to_sleep()

        self.end_of_day()
        self.is_alive()


    # реалізувати в цій функції  вивід на екран номер дня
    # стоврити рандомайзер , який на рандом буде вибирати подію, яку буде
    # робити людина
    # вкінці дня викликати інформацію про його поточні дані
    # зробити перевірку чи живий чи ні



student_Nazar = Student("Nazar")
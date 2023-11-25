from random import *
class Student:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.gladness -= 10
        self.progress += 0.12

    def to_sleep(self):
        print("Sleeping...")
        self.gladness += 3

    def to_chill(self):
        print("REEEEESSSSSSSSTTTTTTTT!!!!!!!")
        self.gladness += 3
        self.progress -= 0.1

    def punishment(self):
        print("INCORECT INPUT (ANGRY)")
        self.progress -= 0.2
        self.gladness -=5

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

        live_choice = input("What will you do today?? "
                            "\n1) Study"
                            "\n2) Chill"
                            "\n3) Sleep"
                            "\nChoice: ")



        if live_choice == "1" or live_choice == "Study" or live_choice == "study":
            self.to_study()

        elif live_choice == "2" or live_choice == "Chill" or live_choice == "chill":
            self.to_chill()

        elif live_choice == "3" or live_choice == "Sleep" or live_choice == "sleep":
            self.to_sleep()

        else:
            self.punishment()

        self.end_of_day()
        self.is_alive()



class Teacher:



class Groups:
    def __init__(self,teacher,students):
        self.teacher = teacher
        self.students = students

teacher_Mariy_Ivanivna = Teacher("Mariya","Ivanivna")

student_Nazar = Student("Nazar")
student_Anna = Student("Anna")
student_Maks = Student("Maks")

students = []

students.append(student_Nazar)
students.append(student_Anna)
students.append(student_Maks)


group1 = Groups("1",teacher_Mariy_Ivanivna,students)


for day in range(7):
    if student_Nazar.alive == False:
        break

    student_Nazar.live(day)

print("GAME OVER!!!")
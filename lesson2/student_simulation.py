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






student_Nazar = Student("Nazar")
class Student:

    def __init__(self,name,age,numberPhone):
        self.name = name
        self.age = age
        self.numberPhone = numberPhone
    def printer(self):
        print("Name of student",self.name)
        print("Age of student", self.age)
        print("Phone Number of student", self.numberPhone)

    def calculateSeconds(self):
        print("Seconds which student life",self.age*365*24*60*60)


first_student = Student("Nazar",20,"38066666")
first_student.printer()
first_student.calculateSeconds()

print()
print()

second_student = Student("Andrew",23,"376764654654")
second_student.printer()
second_student.calculateSeconds()






import datetime
class Human:
    def __init__(self, first_name, last_name, date_of_birth,phoneNumber):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("First name: ",self.first_name,
              "\nLast name: ",self.last_name,
              "\ndate_of_birth",self.date_of_birth,
              "\nphoneNumber",self.phoneNumber)

    def calculate_age(self):
        day_now = datetime.date.today()

        age = day_now.year - self.date_of_birth.year

        if (day_now.month < self.date_of_birth.month or
        (day_now.month == self.date_of_birth.month and day_now.day < self.date_of_birth.day)):

            age -= 1


        return age


class Student(Human):

    def __init__(self,first_name, last_name, date_of_birth,phoneNumber,progress,course):
      super().__init__(first_name,last_name,date_of_birth,phoneNumber)
      self.progress = progress
      self.course = course


    def point5scale(self):
        score = 0
        if self.progress>=1 and self.progress<=3:
            score=1
            print("Your score in 5 point scale: ",score)


class Teacher(Human):
    def __init__(self, first_name, last_name, date_of_birth, phoneNumber, subject,sallary):
        super().__init__(first_name, last_name, date_of_birth, phoneNumber)
        self.subject = subject
        self.sallary = sallary


    def sallaryInDollar(self):

        print("Sallary in dollar $",self.sallary/38)

studentAnna = Student("Anna","Polyanska",datetime.date(2009,11,20),
                      "+3806666666",2,4)

studentAnna.point5scale()

studentAnna.printInfo()

print(studentAnna.calculate_age())


teacherNazar = Teacher("Nazar","Lakusta",datetime.date(2003,10,17),
                       "+38077567676","Python OOP",38000)


teacherNazar.sallaryInDollar()
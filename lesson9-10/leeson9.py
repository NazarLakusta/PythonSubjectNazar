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


class Student(Human):

    def __init__(self,first_name, last_name, date_of_birth,phoneNumber,progress,course):
      super().__init__(first_name,last_name,date_of_birth,phoneNumber)
      self.progress = progress
      self.course = course





class Teacher(Human):
    def __init__(self, first_name, last_name, date_of_birth, phoneNumber, subject,sallary):
        super().__init__(first_name, last_name, date_of_birth, phoneNumber)
        self.subject = subject
        self.sallary = sallary


studentAnna = Student("Anna","Polyanska",datetime.date(2009,11,20),
                      "+3806666666",12,4)


studentAnna.printInfo()z





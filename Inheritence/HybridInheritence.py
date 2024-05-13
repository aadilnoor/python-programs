class School:
    def func1(self):
        print("This function is in school")

class Teacher(School):
    def func2(self):
        print("This function is in teacher")

class Student(School):
    def func3(self):
        print("This function is in student")

class Resident(Teacher, Student):
    def func4(self):
        print("This function is in resident")


obj = Resident()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
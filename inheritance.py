class Human:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Student(Human):
    def speak(self):
        print("Hello")

class Teacher(Human):
    def speak(self):
        print("Good Morning!")

class Principal(Human):
    def speak(self):
        print("Hello Everyone")

student = Student("Marvin")
teacher = Teacher("Charles")
principal = Principal("Marcus")

print(student.name)
print(student.is_alive)
student.eat()
student.sleep()


class Student:

    class_year = 2025
    num_students = 0


    def __init__(self ,name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Marvin", 22)  
student2 = Student("Jane", 26)  
student3 = Student("Marcus", 30)
student4 = Student("Charles", 40)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
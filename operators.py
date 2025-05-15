# students = {"Marvin", "Marcus", "Charles"}
# student = input("Enter the name of a student: ")
# if student in students:
#     print(f"{student} is a student in that school")
# else:
#     print(f"{student} is not a student of that school")


grades = {"Marvin": "A","Marcus": "B","Charles": "C","Camille": "D"  }

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
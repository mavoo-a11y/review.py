# name = input("Enter yor name: ")

# while name == "":
#     print("You didn't enter your name ")
#     name = input("Enter yor name: ")
# print(f"Hello {name}")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif age < 0:
     print("You haven't been born yet")
else:
    print("You are a minor")

def display_instructions():
    print("Welcome to the program")
    print("Please follow the instructions to proceed")
    print("1. Enter your name")
    print("2. Enter your age")
    print("3. Enter your Marital_status")
    print("4. Enter your sex")
    print("5. Enter your Grind")

def get_user_input():
      name = input("Enter your name: ")
      age = int(input("Enter your age: "))
      marital_status = input("Enter your marital status: ")
      sex = input("Enter your sex: ")
      grind = input("Enter your grind: ")

      return name,age,marital_status,sex,grind
    
name,age,marital_status,sex,grind = get_user_input()

def display_user_information(name,age,marital_status,sex,grind):
        print("User information:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Marital_status: {marital_status}")
        print(f"Sex: {sex}")
        print(f"Grind: {grind}")
        print("YOU ARE NOW LOGGED IN")
        print("WELCOME TO THE PROGRAM")

display_instructions()
name,age,marital_status,sex,grind = get_user_input()
display_user_information(name,age,marital_status,sex,grind)


    

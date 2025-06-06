import random
import os
import time

def run_password_cracker():
    u_pwd = input("Enter a password: ")

    pwd_chars = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '1','2','3','4','5','6','7','8','9','0'
    ]

    cracked_password = ""
    attempts = 0

    print("Cracking password....Please wait....")

    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
    print(f"Target password length: {len(u_pwd)}")
    print("Starting brute-force......")

    for i in range(len(u_pwd)):
        found_char = False
        while not found_char:
            guess_char = random.choice(pwd_chars)
            attempts += 1
            if guess_char == u_pwd[i]:
                cracked_password += guess_char
                found_char = True
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")
            print(f"Current guess: {cracked_password + '_' * (len(u_pwd) - len(cracked_password))}")
            time.sleep(0.1)
    
    print(f"Password cracked successfully! The password is: \"{cracked_password}\"")
    print(f"Total attempts: {attempts}")
    print("Time taken: {:.2f} seconds".format(attempts * 0.1))

if __name__ == "__main__":
    run_password_cracker()

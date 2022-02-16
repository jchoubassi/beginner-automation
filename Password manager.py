from cgitb import text
from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")



def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd)


while True:
    mode = input("Would you like to add a new password or view existing ones? (View, add, press q to quit.) ").lower()

    if mode == "q":
        break

    if mode == "view":
        pass

    elif mode == "add":
        pass

    else:
        print("Invalid mode.")
        continue




from cryptography.fernet import Fernet
# get input for master password

pwd = input("Enter master password: ")

if pwd == "password":
    print("Welcome to the password manager")

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

def add():
    pass
    nameofservice = input("Enter the name of the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open ("passwords.txt", "a") as f:
        f.write(nameofservice + " | " + username + " | " + password + "" + '\n' )

def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = print(line.rstrip())
            service, usr, pwd = data.split(" | ")
            print("Service: " + service + " , Username: " + usr + " , Password: " + pwd)

while True:
    choice = input("Would you like to add a new password or view an existing one? Or enter exit to quit (add/view/exit)")

    if choice == "add":
        add()
    elif choice == "view":
        view()
    elif choice == "exit":
        exit()






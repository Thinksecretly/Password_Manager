from cryptography.fernet import Fernet
# get input for master password

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

if master_pwd == "password":
    print("Welcome to the password manager")
else:
    print("Incorrect password")
    exit()




def add():
    nameofservice = input("Enter the name of the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open ("passwords.txt", "a") as f:
        f.write(nameofservice + "|" + username + "|" + str(fer.encrypt(password.encode()).decode()) + "\n")

def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            service, usr, pwd = data.split("|")
            print("Service: " + service + " , Username: " + usr + " , Password: " + fer.decrypt(pwd.encode()).decode())

while True:
    choice = input("Would you like to add a new password or view an existing one? Or enter exit to quit (add/view/exit)").lower

    if choice == "add":
        add()
    elif choice == "view":
        view()
    elif choice == "exit":
        exit()






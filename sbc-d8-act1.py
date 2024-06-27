

def textFile():
    return [line.strip() for line in open("sbc-d8-act1.txt")]

def register():
    username = input("Enter Username: ")
    password = input("Enter password: ")
    file = textFile()
    if username in file:
        print("already exit")
    else:
        with open("sbc-d8-act1.txt", "a") as f:
            f.write(username + "\n")
            f.write(password + "\n")
            print("Account Created Sucessfully")
def login():
    username = input("Username: ")
    password = input("password: ")
    file = textFile()
    if username and password in file:
        print("Log In Sucessfully") 
        print(f"Welcome My Master: {username}")
    else:
        print("Invalid Credentials")

def changePassword():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    file = textFile()
    if username in file:
        index = file.index(username)
        if password == file[index + 1]:
            new_password = input("Enter New Password: ")
            file[index + 1] = new_password
            with open("sbc-d8-act1.txt", "w") as f:
                for line in file:
                    f.write(line + "\n")
            print("Password successfully changed")
        else:
            print("Invalid credentials")
    else:
        print("Invalid credentials")

def main():
    while True:
        print("""
        -----SELECT OPTION-----
            1 : Register
            2 : Login
            3 : Changepassword
            0 : Exit
        """)

        option = input("Enter Selected Option: ")

        if option == '1':
            register()
        elif option == '2':
            login()
        elif option == '3':
            changePassword()
        elif option == '0':
            print("Thank You!")
            exit()
main()
          

from utils import add_password, remove_password, show_passwords

Password_list = []

try:
    with open("password.txt", "r") as file:
        Password_list = [line.strip() for line in file]
        print("Loaded succesfully")
except FileNotFoundError:
    print("Could'nt find the file")

def main():
    while True:
        User_input = int(input("What do you want to do? enter the number: \n 1:Add a password \n 2:Remove a password \n 3:See your passwords \n 4: Save and quit \n"))
        match User_input:
            case 1:
                add_password(Password_list)
            case 2: 
                remove_password(Password_list)
            case 3:
                show_passwords(Password_list)
            case 4: 
                with open("password.txt", "w") as file:
                    for password in Password_list:
                        file.write(password +"\n")
                    print("Passwords saved succesfully")
                    break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()
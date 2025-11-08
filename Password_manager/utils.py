def add_password(Password_list):
    User_name = input("What is the username? ")
    Password = input("What is the password? ")
    Source = input("What is it for? ")
    Information = Source + ": " + User_name + " | " + Password
    Password_list.append(Information)
    print("Password saved succesfully")
    return Password_list



def remove_password(Password_list):
    Source = input("What is the source of the password you want to remove?\n")
    found = False

    for entry in Password_list:
        if Source.lower() in entry.lower():
            Password_list.remove(entry)
            print(f"Removed '{entry}' successfully.")
            found = True
            break

    if not found:
        print("Couldn't find that source.")


def show_passwords(Password_list):
    if Password_list:
        print("These are your usernames and passwords: \n", ", ".join(Password_list))
    else:
        print("List is empty")



                       


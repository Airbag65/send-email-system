import json
from getpass import getpass

# Strings
name = ""
password = ""
password_email = ""
# Confirmation needs to be different from beginning for program to run
confirm_password = "1"
confirm_password_email = "1"

# Dictionary for new account
new_account = {}


def create_account():
    global name, password, confirm_password, new_account
    name = input(
        "\nSelect the name of the new account. \nMake sure to double check if it's correct before submiting! \nEnter the name of the account: "
        )
    create_password()
    if password != confirm_password:
        print("\nThe passwords do not match!\nTry again!\n")
        create_password()
    
    email = input("\nEnter the email-adress you want to link to the account.\nOnce again, make sure it is correct before confirming! \nEnter email-adress: ")
    create_email_password()
    if password_email != confirm_password_email:
        print("\nThe passwords do not match!\nTry again!\n")
        create_email_password()
    new_account = {'name': f'{name}','password': f'{password}', 'email': f'{email}', 'email-password': f'{password_email}'}

    with open ("emails.json", "r") as open_file:
        data = json.load(open_file)
        open_file.close()

    data['accounts'].append(new_account)

    write_file = open("emails.json", "w+")
    write_file.write(json.dumps(data, indent = 4, sort_keys = True))
    write_file.close()
    

def create_password():
    global password, confirm_password
    print("\nSelect a password for the new account.")
    password = getpass("\nEnter new password: ")  
    confirm_password = getpass("Please confirm the password: ")

def create_email_password():
    global password_email, confirm_password_email
    print("\nEnter the password for the email")
    password_email = getpass("\nEnter password: ")  
    confirm_password_email = getpass("Please confirm the password: ")
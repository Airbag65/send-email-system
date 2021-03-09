from time import sleep
import json
import open_json
import add_account
from getpass import getpass

# Booleans
logged_in = False
account_found = False

# Strings
chosen_account = ""
active_account = ""
active_password = ""
relevant_email = ""
relevant_email_password = ""
relevant_contacts = ""
relevant_message = ""
user_choice = ""

# Integers
num = -1

# Imported arrays from open_json.py
available_accounts = []
possible_passwords = []

to_return = []


def choose_account():
    global available_accounts, chosen_account, possible_passwords, active_account, active_password, num, account_found, relevant_email, relevant_email_password, to_return, relevant_contacts, relevant_message

    available_accounts = open_json.open_json()[0]
    possible_passwords = open_json.open_json()[1] 
    email_adresses = open_json.open_json()[2]
    email_passwords = open_json.open_json()[3]
    contacts = open_json.open_json()[4]
    messages = open_json.open_json()[5]

    num = -1
    print("\nAvailable accounts: ")
    for i in available_accounts:
        print(i)
    print("")
    chosen_account = input("Type the name of the account you want to log into: ")
    for i in available_accounts:
        num += 1
        if chosen_account.lower() == i.lower():
            chosen_account = i
            active_account = available_accounts[num]
            active_password = possible_passwords[num]
            relevant_email = email_adresses[num]
            relevant_email_password = email_passwords[num]
            relevant_contacts = contacts[num]
            relevant_message = messages[num]

            to_return.append(active_account)
            to_return.append(active_password)
            to_return.append(relevant_email)
            to_return.append(relevant_email_password)
            to_return.append(relevant_contacts)
            to_return.append(relevant_message)

            account_found = True
            print("Account Found!\nEnter the password for " + chosen_account + "\n")
        else:
            account_found = False

        if account_found:
            break
        else:
            continue
    if account_found == False:
        print("\nAccount not Found!\nTry Again!")


def logging_in():
    global logged_in
    global active_password
    user_input = getpass("Password: ")
    if user_input == active_password:
        logged_in = True
        print("\nLogging in...\n")
        sleep(.5)
    else:
        print("\nPassword was incorrect\nTry again\n")
        sleep(.5)


def system():
    print("\nWelcome! \n")


def run():
    global logged_in, chosen_account, account_found, user_choice, to_return

    user_choice = input("Do you want to log into an existing account or create a new account? [L/C]: ")
    if user_choice.lower() == 'l':
        print("")
    elif user_choice.lower() == 'c':
        add_account.create_account()

    while account_found == False:
        choose_account()
    while logged_in == False:
        logging_in()
    if logged_in:
        return to_return

import json
import open_json
import login
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

user_info = []
user_name = ""
user_password = ""
user_email = ""
user_email_password = ""
names = []
emails = []
message = ""
message_body = ""
receiving_adress = ""
receiver_name = ""
receiver = ""
adress_found = False
email_subject = ""
index = 0
send_message_selection = ""

s = smtplib.SMTP(host='smtp.gmail.com', port=587)

def user_information():
    global user_name, user_password, user_email, user_email_password
    login.run()
    user_name = login.to_return[0]
    user_password = login.to_return[1]
    user_email = login.to_return[2]
    user_email_password = login.to_return[3]


def login_mail():
    global s, user_email, user_email_password
    s.starttls()
    s.login(user_email,user_email_password)


def get_contact(filename):
    global names, emails
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def select_receiver():
    global receiving_adress, adress_found, index, receiver, receiver_name
    index = -1
    receiver = input("Type the name you want to send an email to: ")
    for i in names:
        index += 1
        if i.lower() == receiver.lower():
            receiver = i
            print(receiver)
            receiving_adress = emails[index]
            receiver_name = names[index]
            adress_found = True
            print("\nReceiver selected!\n")
        else:
            adress_found = False
        
        if adress_found:
            break
        else:
            continue
    if adress_found == False:
        print("\nReceiver not Found!\nTry Again!\n")
        select_receiver()
    receiver_name = receiver


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def construct_email():
    global names, emails, message, message_body, user_email, receiving_adress, adress_found, email_subject, index, receiver, receiver_name
    message = MIMEMultipart()

    print("Who do you want to send your mail to?\nYour contacts: ")
    for name in names:
        print(name)
    
    select_receiver()

    email_subject = input("Type the subject of your email: ")
    message_template = read_template("./message.txt")

    message_body = message_template.substitute(receiver = receiver_name.title())

    message['From'] = user_email
    message['To'] = receiving_adress
    message['Subject'] = email_subject
    message['Message'] = message_body

    message.attach(MIMEText(message_body))

    print("\nYour Message:\n\n")
    print(message)
    print("\n\n")

    return message
    

def send_email():
    global s, send_message_selection
    user_information()
    login_mail()
    get_contact("./contacts.txt")
    meddelande = construct_email()
    comfirm_send = input("Do you want to confirm and send the mail? [y/n]: ")
    if comfirm_send.lower() == "y":
        s.send_message(meddelande) 
        print("\n\nMessage has been sent! \n\n")
        send_message_selection = True
    elif comfirm_send.lower() == "n":
        print("\n\nTask Canceled!\nMessage was not sent!\n\n")
        send_message_selection = True
    else:
        print("\n\nTask was not confirmed and has therefore been canceled!\nMessage was not sent!\n\n")
        send_message_selection = True

    while send_message_selection:
        end_program = input("\n\nPress ENTER to stop the program: \n\n\n")
        if end_program == "":
            send_message_selection = False
        else:
            send_message_selection = False

send_email()
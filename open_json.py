import json

def open_json():
    with open ("emails.json", "r") as opened:
        data = json.load(opened)

    accounts = []

    names = []
    passwords = []
    emails = []
    email_passwords = []

    for i in data["accounts"]:
        accounts.append(i)

    for account in accounts:
        names.append(account['name'])
        passwords.append(account['password'])
        emails.append(account['email'])
        email_passwords.append(account['email-password'])

    to_return = [names, passwords, emails, email_passwords]

    return to_return

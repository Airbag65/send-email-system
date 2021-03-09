# send-email-system
This is a little system that builds on the login system I have
previously created. To use the system you just simply run the send_mail.py file
in your commandprompt for example (provided you have python installed on your system). 
To add more contacts you simply follow the template in the contacts-txt file, i.e.
type the name of the contact followed by a space and then their email-adress. 

## open_json.py
This files' only purpose is to open the json file, take the data from it and store 
in separate variables (arrays) to then be returned and used by the rest of the program.

## email.json
This is the json file that stores the information about the different users. 

## create_account.py
This file has the functions that are included in creating new account and add them to the list
of accounts in the json file.

## login.py
This is pretty much the same code as the login.py file from my login-system repo. It's 
purpose is to sense which account has been selected by the user, checks to see if the 
password the user enters is correct. If it is, the file returns all the other details 
that are conected to the logged in account. 

## send_email.py
This file handles the main part of the program and ties all the other files togehter.
It is also responsible for constructing an email and send it to the correct reciever. 

## Update 9 March 2021
The different accounts do now have their own contacts and message files. This enables the 
program to be used by as many users as are registered, independently from one another. 
A new file for contacts and message is also being created with the new account when one 
is made. Note that the feature to open and edit the active message file only works on windows
at this current state. To fix this you can however change the program selected to open the file in
(send_email.py, line 103) to something other than notepad.

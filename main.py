#--------------------------------------------------------------------#
#                           Pr0fess0r#1524                           #
#--------------------------------------------------------------------#

import fbchat
from fbchat import Client #/! Importing the CHATBOT
from fbchat.models import Message
import os
import time 

os.system('cls')
#/! Facebook Details

username = input("What's your Facebook Email/Username: ")
password = input("What's your Facebook Password: ")
os.system('cls')

#/! Login

client = Client(username, password) #/! Logging in
time.sleep(1) #/! Wait 1 seccond

os.system('cls')

persontomessage = input("User name of the person you want to message: ") #/! Entering the username
os.system('cls')

users = client.searchForUsers(persontomessage) #/! Searching
user = users[0]

print("Name: {}".format(user.name)) #/! Printing the Entered username's name!

print("User ID: {}".format(user.uid)) #/! Printing the Entered User ID name!

uid = input("Input the User's ID From Above: ") #/! Input the user ID
message = input("Enter your message: ") #/! Message

sendmessage = client.send(Message(text=message), thread_id=uid) #/! Message Sending

os.system('cls')

if sendmessage:
    print("...        ...")
    print("..          ..")
    print(".     --     .")
    print("Message Sent!")
    print(".     --     .")
    print("..          ..")
    print("...        ...")
else:
    print("...        ...")
    print("..          ..")
    print(".     --     .")
    print("Failed to Send")
    print(".     --     .")
    print("..          ..")
    print("...        ...")

time.sleep(2)
os.system('cls')

#--------------------------------------------------------------------#
#                           Pr0fess0r#1524                           #
#--------------------------------------------------------------------#

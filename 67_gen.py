from functions import sendMsgs
from dotenv import load_dotenv
import os
import time
import random


load_dotenv()  # loads the .env file
# List of friends' IDs to send messages to
friends_list = []
friends_list = list(set(friends_list))
# your discord token
yourToken = os.getenv("DISCORD_TOKEN") # Make sure to set the DISCORD_TOKEN environment variable in your .env file

if not yourToken:
    raise ValueError("DISCORD_TOKEN not found in environment variables.")

msg = input("Enter your message (or press enter to abort): ")     

for friend in friends_list:
    if msg =="":
        break
    else:
        delay = random.uniform(2.5, 4.0)

        sendMsgs(yourToken,friend,msg)
        
        print(f"Waiting before messaging next friend...")

        time.sleep(delay)
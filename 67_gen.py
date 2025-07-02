from functions import sendMsgs
# List of friends' IDs to send messages to
friends_list = []
# your discord token
# Replace with your actual token
yourToken = ""

for friend in friends_list:
    # put your actual message here
    #heres my placeholder
    msg = input("Enter your message: ")
    sendMsgs(yourToken,friend,msg)
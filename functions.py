import json
import requests

def sendMsgs(myToken:str,friendID: str, msg: str):
    """
    Sends a message to a friend.

    Parameters:
    friendID (str): The ID of the friend to send the message to.
    msg (str): The message to send.

    Returns:
    None
    """
    
    response1 = requests.post("https://discord.com/api/v10/users/@me/channels", headers = {
        "Authorization": myToken,
        "Content-Type": "application/json"
    }, json = {"recipient_id": friendID})
    
    channel_id = response1.json().get("id",{})
    
    response2 = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/messages"
    ,headers = {
        "Authorization": myToken,
        "Content-Type": "application/json"
    }, json = {"content": msg} )
    
    print(response2.status_code)

    friendName = response1.json().get("recipients", [{}])[0].get("username", "Unknown User")    
    user = response2.json().get("author", {}).get("username", "")
    print(f"{user} is sending a message to {friendName}: {msg}")


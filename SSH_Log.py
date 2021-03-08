#!/usr/bin/python3
import requests, os
from datetime import datetime

Web_Hook = "https://discord.com/api/webhooks/818271927411146842/OYlPe2zRlW9etqbqjKfxJvrWZbL2-PYwvu45Z9P_xV4uscSALqZBVojaEg3b_Co3QLwQ"

embed = {
	"color": 12976176, 
	"title": "SSH-Notification",
    "description": "text in embed",
    "thumbnail": { "url": "https://icons.iconarchive.com/icons/blackvariant/button-ui-system-apps/512/Terminal-icon.png" },
    "footer": { "icon_url": "https://icons.iconarchive.com/icons/blackvariant/button-ui-system-apps/512/Terminal-icon.png", "text": "SSH Notify" },
    "description": "**Details**\n👤 User: "+ os.getlogin() + "\n🕐 Time: "+ str(datetime.now().strftime('%H:%M') + "\n📆 Date: "+ datetime.today().strftime('%Y-%m-%d') + "\n💻 Server IP: "+ str(requests.get('https://api.ipify.org').text) + "\n🕵️ Login IP: "+ os.environ.get("SSH_CONNECTION").split(" ")[2])
    }

data = {
    "username": "SSH Notify",
    "avatar_url": "https://icons.iconarchive.com/icons/blackvariant/button-ui-system-apps/512/Terminal-icon.png",
    "embeds": [
        embed
        ],
}

def Main():
    result = requests.post(Web_Hook, json=data)
    if 200 <= result.status_code < 300:
        pass
    else:
        f =  open("SSH_Log.log", "w")
        f.write(e)

Main()

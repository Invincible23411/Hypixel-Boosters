import string
import requests
from mojang import MojangAPI
import json

userinput = str(input("Would you like to know the current hypixel boosters? "))

requestlink = str("https://api.hypixel.net/boosters?key=1991b8be-199e-4f78-97f0-c1e306dbf07b")

bsdata = requests.get(requestlink).json()

booster_length = len(bsdata["boosters"])

for i in range(0,booster_length):
    player = bsdata["boosters"][i]
    player2 = player["purchaserUuid"]
    amount = int(player["amount"])
    time_left = player["length"]

    url_string = "https://sessionserver.mojang.com/session/minecraft/profile/"+player2

    data = requests.get(url_string).json()

    print(f"The player", (data["name"]), "has boosted", (amount), "times and has", (time_left), "seconds left")


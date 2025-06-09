import time
import pandas
import requests


def main():
    cards = pandas.read_excel("ImportedCards.ods",engine="odf",dtype=str)
    cards.fillna("", inplace = True)
    for card_name in cards.get("name"):
        print("Importing "+ card_name)
        card = cards['name'] == card_name
        request = {"username": "*****","password": "***************",
                   "action": "Upload card", "name": card_name, "type": cards.loc[card, "type"].to_numpy()[0],
                   "effect": cards.loc[card, "effect"].to_numpy()[0], "card_type": cards.loc[card, "card type"].to_numpy()[0], "rush": 0, "limit": 3, "privacy": 1, 
                   "monster_color": cards.loc[card, "color"].to_numpy()[0], "attribute": cards.loc[card, "attribute"].to_numpy()[0],
                   "level": cards.loc[card, "level"].to_numpy()[0], "atk": cards.loc[card, "atk"].to_numpy()[0], "def": cards.loc[card, "def"].to_numpy()[0],
                   "flip":cards.loc[card, "flip"].to_numpy()[0],"ability":cards.loc[card, "ability"].to_numpy()[0]}
        print("GET: "+str(request)+"\nFrom https://api.duelingbook.com/upload-custom-card")
        request["password"] = "****"
        print("Returns: "+str((info := requests.get("https://api.duelingbook.com/upload-custom-card", request)).status_code))
        print(info.content)
        time.sleep(3)




if __name__ == "__main__":
    main()

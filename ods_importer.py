import file_io
import pandas
card_list = file_io.read_json("allCards.json").copy()
cards_data = {}
remove_list = ["Fusion","Link","Synchro","Ritual","Monster","XYZ","Flip","Normal","Pendulum","Effect"]

def order_cards():
    for card in card_list:
        key = card.get("name")
        cards_data[key] = card

def main():
    pandas.options.mode.copy_on_write = True
    order_cards()
    cards = pandas.read_excel("ImportedCards.ods",engine="odf", dtype=str)
    print(cards.to_string())
    print(cards.get("type"))
    for card_name in cards.get("name"):
        print(card_name)
        print(card_entry := cards['name'] == card_name)
        card = cards_data.get(card_name)
        cards.loc[card_entry,"effect"] = card.get("desc")
        cards.loc[card_entry, "type"] = card.get("race")
        type_list = card.get("type").split(" ")
        cards.loc[card_entry, "card type"] = type_list[0]
        if type_list[0] != "Spell" and type_list[0] != "Trap":
            cards.loc[card_entry, "card type"] = "Monster"
            cards.loc[card_entry, "color"] = type_list[0]
            if type_list[0] not in remove_list or type_list[0] == "Pendulum" or type_list[0] == "Flip":
                cards.loc[card_entry, "color"] = "Effect"
            cards.loc[card_entry, "attribute"] = card.get("attribute")
            cards.loc[card_entry, "level"] = card.get("level")
            cards.loc[card_entry, "atk"] = card.get("atk")
            cards.loc[card_entry, "def"] = card.get("def")
            if card.get("atk") == -1:
                cards.loc[card_entry, "atk"] = "?"
            if card.get("def") == -1:
                cards.loc[card_entry, "def"] = "?"
            if "Flip" in type_list:
                cards.loc[card_entry, "flip"] = 1
            for item in remove_list:
                try:
                    type_list.remove(item)
                except:
                    pass
            if len(type_list) > 0:
                cards.loc[card_entry, "ability"] = type_list
        cards.loc[card_entry, "id"] = int(card.get("id"))
        print(cards.loc[cards['name'] == card_name])
    cards.to_excel("ImportedCards.ods", engine="odf", index=False)
"""

is_effect


pendulum


scale


pendulum_effect


arrows

"""




if __name__ == "__main__":
    main()

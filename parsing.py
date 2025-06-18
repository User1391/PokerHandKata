import data_structures


def face_string_to_int(face_string):
    match face_string:
        case "T":
            return 10
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14
        case _:
            return int(face_string)


def card_string_to_card(card_str):
    return data_structures.Card(face_string_to_int(card_str[0]), card_str[1])


def string_of_cards_to_list_of_cards(string_of_cards):
    deck = []
    for card_str in string_of_cards.split():
        deck.append(card_string_to_card(card_str))
    return deck

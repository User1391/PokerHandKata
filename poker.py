
def face_string_to_int(face_string):
    match face_string:
        case 'T':
            return 10
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14
        case _:
            return int(face_string)

def face_int_to_string(face_int):
    if face_int < 10:
        return str(face_int)
    else:
        match face_int:
            case 10:
                return 'T'
            case 11:
                return 'J'
            case 12:
                return 'Q'
            case 13:
                return 'K'
            case 14:
                return 'A'


def string_of_cards_to_list_of_cards(string_of_cards):
    deck = []
    for card_str in string_of_cards.split():
        deck.append(Card(card_str))
    return deck


def is_hand_pair(poker_hand):
    for card_idx in range(len(poker_hand) - 1):
        if poker_hand.cards[card_idx].face == poker_hand.cards[card_idx + 1].face:
            return True
    return False

def is_hand_two_pair(poker_hand):
    pair_cnt = 0
    for card_idx in range(len(poker_hand) - 1):
        if poker_hand.cards[card_idx].face == poker_hand.cards[card_idx + 1].face:
            pair_cnt += 1
    return True if pair_cnt >= 2 else False

def is_hand_three_of_a_kind(poker_hand):
    for card_idx in range(len(poker_hand) - 2):
        if poker_hand.cards[card_idx].face == poker_hand.cards[card_idx + 1].face == poker_hand.cards[card_idx + 2].face:
            return True
    return False

def is_hand_straight(poker_hand):
    first_val = poker_hand.cards[0].face 
    for card_face, card in zip(range(first_val + 1, first_val + len(poker_hand)), poker_hand.cards[1:]):
        if card_face != card.face:
            return False 
    return True

def is_hand_flush(poker_hand):
    sample_suit = poker_hand.cards[0].suit 
    for card_idx in range(1, len(poker_hand.cards)):
        if poker_hand.cards[card_idx].suit != sample_suit:
            return False
    return True

def is_hand_full_house(poker_hand):
    cards = poker_hand.cards 
    if cards[0].face == cards[2].face and cards[3].face == cards[4].face:
        return True
    elif cards[0].face == cards[1].face and cards[2].face == cards[4].face:
        return True 
    else:
        return False

def is_hand_four_of_a_kind(poker_hand):
    cards = poker_hand.cards 
    return cards[0].face == cards[3].face or cards[1].face == cards[4].face 

def is_hand_straight_flush(poker_hand):
    return is_hand_straight(poker_hand) and is_hand_flush(poker_hand)

def hand_type(poker_hand):
    if is_hand_straight_flush(poker_hand):
        return "Straight Flush"
    elif is_hand_four_of_a_kind(poker_hand):
        return "Four of a Kind"
    elif is_hand_full_house(poker_hand):
        return "Full House"
    elif is_hand_flush(poker_hand):
        return "Flush"
    elif is_hand_straight(poker_hand):
        return "Straight"
    elif is_hand_three_of_a_kind(poker_hand):
        return "Three of a Kind"
    elif is_hand_two_pair(poker_hand):
        return "Two Pair"
    elif is_hand_pair(poker_hand):
        return "Pair"
    else:
        return "High Card"

class Card:
    def __init__(self, card_str):
        self.face = face_string_to_int(card_str[0])
        self.suit = card_str[1]

    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit

    def __str__(self):
        return "Card(" + str(self.face) + self.suit + ")"

    


class PokerHand:
    def __init__(self, list_of_cards):
        self.cards = sorted(list_of_cards, key=lambda x: x.face)
    def __eq__(self, other):
        for my_card, other_card in enumerate(zip(self.cards, other.cards)):
            if my_card != other_card:
                return False
        return True
    def __str__(self):
        out_str = "PokerHand["
        for card in self.cards:
            out_str += face_int_to_string(card.face) + card.suit
            if card != self.cards[-1]:
                out_str += " "
        return out_str + "]"
    def __len__(self):
        return len(self.cards)
            


            




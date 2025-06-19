import data_structures as ds
import poker_rank as pr


def hand_type(poker_hand: ds.PokerHand) -> str:
    if pr.is_hand_straight_flush(poker_hand):
        return "Straight Flush"
    elif pr.is_hand_four_of_a_kind(poker_hand):
        return "Four of a Kind"
    elif pr.is_hand_full_house(poker_hand):
        return "Full House"
    elif pr.is_hand_flush(poker_hand):
        return "Flush"
    elif pr.is_hand_straight(poker_hand):
        return "Straight"
    elif pr.is_hand_three_of_a_kind(poker_hand):
        return "Three of a Kind"
    elif pr.is_hand_two_pair(poker_hand):
        return "Two Pair"
    elif pr.is_hand_pair(poker_hand):
        return "Pair"
    else:
        return "High Card"


def face_int_to_string(face_int):
    if face_int < 10:
        return str(face_int)
    else:
        match face_int:
            case 10:
                return "T"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case 14:
                return "A"


def hand_to_string(hand: ds.PokerHand):
    out_str = "PokerHand["
    for card in hand.cards:
        out_str += face_int_to_string(card.face) + card.suit
        if card != hand.cards[-1]:
            out_str += " "
    return out_str + "]"


def card_to_string(card: ds.Card):
    return "Card(" + str(card.face) + card.suit + ")"


def deck_to_string(deck: ds.Deck):
    out_str = "Deck["
    for card in deck.deck:
        out_str += card_to_string(card)
        if card != deck.deck[-1]:
            out_str += " "
    return out_str + "]"


def player_to_string(player: ds.Player):
    return player.name + ": " + hand_to_string(player.hand)

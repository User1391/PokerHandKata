from poker_rank import *
from data_structures import *
from hand_comparer import *
from parsing import *
from display import *
import random

# Testing Basic Card Parsing
my_card1 = card_string_to_card("2H")
assert my_card1.face == 2
assert my_card1.suit == "H"

# Testing Card Parsing with Face Card
my_card2 = card_string_to_card("KD")
assert my_card2.face == 13
assert my_card2.suit == "D"

# Testing Overall Hand Parsing & Sorting
my_hand1 = "2H 3D 9S 5C KD"
my_hand1 = string_of_cards_to_list_of_cards(my_hand1)
my_hand1_class = PokerHand(my_hand1)
assert hand_to_string(my_hand1_class) == "PokerHand[2H 3D 5C 9S KD]"

# Testing for Pair
my_hand = "4D 2H 5S AD AH"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_pair(my_hand) == True

# Testing for Two Pair
assert is_hand_two_pair(my_hand) == False
my_hand = "4D 4H 5S AD AH"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_two_pair(my_hand) == True

# Testing for Three of a Kind
assert is_hand_three_of_a_kind(my_hand) == False
my_hand = "5S 5H 5D AD 4C"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_three_of_a_kind(my_hand) == True

# Testing for Straight
my_hand = "4D 5S 6H 8C 7S"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_straight(my_hand) == True

# Testing for Flush
my_hand = "3D 5D 2D TD QD"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_flush(my_hand) == True

# Testing for Full House
my_hand = "3D 3H 3S 2C 2H"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_full_house(my_hand) == True

# Testing for Quads (Four of a Kind)
my_hand = "KD KH KS KC 2S"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_four_of_a_kind(my_hand) == True

# Testing for Straight Flush
my_hand = "9D TD JD QD KD"
my_hand = string_of_cards_to_list_of_cards(my_hand)
my_hand = PokerHand(my_hand)
assert is_hand_straight_flush(my_hand) == True

# Testing Hand Type
deck = []
for face in range(2, 14):
    for suit in ["D", "H", "C", "S"]:
        deck.append(Card(face, suit))

for i in range(10):
    hand = random.sample(deck, 5)
    hand = PokerHand(hand)
    print(hand_to_string(hand))
    print(hand_type(hand))

# Testing Hand Comparisons (opponent hand stronger)
my_hand = "2H 3D 5S 9C KD"
oppo_hand = "2C 3H 4S 8C AH"
my_hand = string_of_cards_to_list_of_cards(my_hand)
oppo_hand = string_of_cards_to_list_of_cards(oppo_hand)
my_hand = PokerHand(my_hand)
oppo_hand = PokerHand(oppo_hand)
assert hand_stronger(my_hand, oppo_hand) == -1

# Testing Hand Comparisons (my hand stronger)
my_hand = "2H 4S 4C 2D 4H"
oppo_hand = "2S 8S AS QS 3S"
my_hand = string_of_cards_to_list_of_cards(my_hand)
oppo_hand = string_of_cards_to_list_of_cards(oppo_hand)
my_hand = PokerHand(my_hand)
oppo_hand = PokerHand(oppo_hand)
assert hand_stronger(my_hand, oppo_hand) == 1

# Testing Hand Comparisons (tie)
my_hand = "2H 3D 5S 9C KD"
oppo_hand = "2D 3H 5C 9S KH"
my_hand = string_of_cards_to_list_of_cards(my_hand)
oppo_hand = string_of_cards_to_list_of_cards(oppo_hand)
my_hand = PokerHand(my_hand)
oppo_hand = PokerHand(oppo_hand)
assert hand_stronger(my_hand, oppo_hand) == 0


print("All tests passed.")

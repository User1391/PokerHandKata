class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit


class PokerHand:
    def __init__(self, list_of_cards):
        self.cards = sorted(list_of_cards, key=lambda x: x.face)

    def __eq__(self, other):
        for my_card, other_card in zip(self.cards, other.cards):
            if my_card.face != other_card.face:
                return False
        return True

    def __gt__(self, other):
        # I am aware there may be a better way to do this than fully reversing, but it is
        # just not a meaningful compute time difference
        for my_card, other_card in zip(reversed(self.cards), reversed(other.cards)):
            if my_card.face > other_card.face:
                return True
            elif my_card.face < other_card.face:
                return False

    def __len__(self):
        return len(self.cards)

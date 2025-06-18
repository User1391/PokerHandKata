import data_structures as ds


def is_hand_pair(poker_hand: ds.PokerHand) -> bool:
    for card_idx in range(len(poker_hand) - 1):
        if poker_hand.cards[card_idx].face == poker_hand.cards[card_idx + 1].face:
            return True
    return False


def is_hand_two_pair(poker_hand: ds.PokerHand) -> bool:
    pair_cnt = 0
    for card_idx in range(len(poker_hand) - 1):
        if poker_hand.cards[card_idx].face == poker_hand.cards[card_idx + 1].face:
            pair_cnt += 1
    return True if pair_cnt >= 2 else False


def is_hand_three_of_a_kind(poker_hand: ds.PokerHand) -> bool:
    for card_idx in range(len(poker_hand) - 2):
        if (
            poker_hand.cards[card_idx].face
            == poker_hand.cards[card_idx + 1].face
            == poker_hand.cards[card_idx + 2].face
        ):
            return True
    return False


def is_hand_straight(poker_hand: ds.PokerHand) -> bool:
    first_val = poker_hand.cards[0].face
    for card_face, card in zip(
        range(first_val + 1, first_val + len(poker_hand)), poker_hand.cards[1:]
    ):
        if card_face != card.face:
            return False
    return True


def is_hand_flush(poker_hand: ds.PokerHand) -> bool:
    sample_suit = poker_hand.cards[0].suit
    for card_idx in range(1, len(poker_hand.cards)):
        if poker_hand.cards[card_idx].suit != sample_suit:
            return False
    return True


def is_hand_full_house(poker_hand: ds.PokerHand) -> bool:
    cards = poker_hand.cards
    if cards[0].face == cards[2].face and cards[3].face == cards[4].face:
        return True
    elif cards[0].face == cards[1].face and cards[2].face == cards[4].face:
        return True
    else:
        return False


def is_hand_four_of_a_kind(poker_hand: ds.PokerHand) -> bool:
    cards = poker_hand.cards
    return cards[0].face == cards[3].face or cards[1].face == cards[4].face


def is_hand_straight_flush(poker_hand: ds.PokerHand) -> bool:
    return is_hand_straight(poker_hand) and is_hand_flush(poker_hand)


def hand_type_rank(poker_hand):
    if is_hand_straight_flush(poker_hand):
        return 8
    elif is_hand_four_of_a_kind(poker_hand):
        return 7
    elif is_hand_full_house(poker_hand):
        return 6
    elif is_hand_flush(poker_hand):
        return 5
    elif is_hand_straight(poker_hand):
        return 4
    elif is_hand_three_of_a_kind(poker_hand):
        return 3
    elif is_hand_two_pair(poker_hand):
        return 2
    elif is_hand_pair(poker_hand):
        return 1
    else:
        return 0

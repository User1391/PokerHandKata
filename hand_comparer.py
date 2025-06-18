import poker_rank
import data_structures


def hand_stronger(
    hand: data_structures.PokerHand, opponent_hand: data_structures.PokerHand
) -> int:
    ht_rank = poker_rank.hand_type_rank(hand)
    oppo_ht_rank = poker_rank.hand_type_rank(opponent_hand)

    if ht_rank > oppo_ht_rank:
        return 1
    elif ht_rank < oppo_ht_rank:
        return -1
    elif hand == opponent_hand:
        return 0
    # actually need to find the high card
    # because the flush parity has already been checked, we can just compare faces (ranks)
    else:
        return 1 if hand > opponent_hand else -1

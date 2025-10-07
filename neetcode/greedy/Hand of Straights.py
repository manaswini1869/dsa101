class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        freq_map = {}
        for i in hand:
            freq_map[i] = freq_map.get(i, 0) + 1

        hand.sort()

        for card in hand:
            if freq_map[card]:
                for next_card in range(card, card + groupSize):
                    if freq_map.get(next_card, 0) == 0:
                        return False

                    freq_map[next_card] -= 1

        return True

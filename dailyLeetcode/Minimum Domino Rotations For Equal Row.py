class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        for target in [tops[0], bottoms[0]]:
            missingT, missingB = 0, 0
            for i, pair in enumerate(zip(tops, bottoms)):
                top, bottom = pair
                if not (top == target or bottom == target):
                    break
                if top != target : missingT += 1
                if bottom != target : missingB += 1
                if i == len(tops) - 1:
                    return min(missingT, missingB)
        return -1

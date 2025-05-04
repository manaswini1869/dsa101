from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        hashd = defaultdict(int)
        n = len(dominoes)
        for a, b in dominoes:
            key = tuple(sorted((a,b)))
            count += hashd[key]
            hashd[key] += 1
        return count
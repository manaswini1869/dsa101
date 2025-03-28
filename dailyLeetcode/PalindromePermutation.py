from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hash_s = Counter(s)
        count_odd = 0
        for _, value in hash_s.items():
            if value % 2 != 0:
                count_odd += 1
        return count_odd <= 1
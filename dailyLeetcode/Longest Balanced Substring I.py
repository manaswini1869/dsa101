from collections import defaultdict
class Solution:
    def longestBalanced(self, s: str) -> int:

        n = len(s)
        max_size = 1
        counter = defaultdict(int)
        for i in range(n):
            counter[s[i]] += 1
            for j in range(i+1, n):
                counter[s[j]] += 1
                if len(set(counter.values())) == 1:
                    max_size = max(max_size, j-i+1)
            counter = defaultdict(int)
        return max_size


        # time complexity = O(n**2)
        # space complexity = O(n)



        
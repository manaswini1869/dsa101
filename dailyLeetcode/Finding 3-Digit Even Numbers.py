class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # ans = set()
        # n = len(digits)
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if i == j or j == k or i == k:
        #                 continue
        #             num = digits[i] * 100 + digits[j] * 10 + digits[k]
        #             if num >= 100 and num % 2 == 0:
        #                 ans.add(num)
        # ans1 = list(ans)
        # return sorted(ans1)
        ans = []
        freq = Counter(digits)
        for i in range(100, 1000, 2):
            freq1 = Counter([int(d) for d in str(i)])
            if all(freq[d] >= freq1[d] for d in freq1.keys()):
                ans.append(i)
        return ans
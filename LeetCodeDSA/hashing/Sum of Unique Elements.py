class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0

        unique = defaultdict(int)

        for num in nums:
            unique[num] += 1

        for k, v in unique.items():
            if v == 1:
                ans += k

        return ans

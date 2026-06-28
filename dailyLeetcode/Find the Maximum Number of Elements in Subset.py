class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        ans = 0

        ans = mapping[1] - (mapping[1] % 2 ^ 1)
        del mapping[1]

        for num in nums:
            temp = 0
            x = num
            while mapping[x] > 1:
                temp += 2
                x *= x
            if mapping[x]:
                temp += 1
            else:
                temp -= 1
            ans = max(ans, temp)
        return ans


        
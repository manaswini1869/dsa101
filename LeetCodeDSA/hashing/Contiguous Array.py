class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        mapper = defaultdict(int)
        mapper[0] = -1
        res = 0
        prefix = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                prefix += 1
            else:
                prefix -= 1

            if prefix in mapper:
                res = max(res, i - mapper[prefix])
                print(res)
            else:
                mapper[prefix] = i

        return res




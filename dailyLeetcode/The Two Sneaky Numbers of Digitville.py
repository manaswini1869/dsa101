

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        res = []
        mapper = defaultdict(int)
        n = len(nums)
        # nums.sort()
        for i in range(n):
            if mapper[nums[i]] == 1:
                res.append(nums[i])
            mapper[nums[i]] += 1

        return res



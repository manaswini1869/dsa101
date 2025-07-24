class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # res = []
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if j != i and nums[j] < nums[i]:
        #             count += 1

        #     res.append(count)
        # return res
        temp = sorted(nums)
        temp_dict = {}

        for k, v in enumerate(temp):
            if v not in temp_dict:
                temp_dict[v] = k

        res = []
        for num in nums:
            res.append(temp_dict[num])
        return res
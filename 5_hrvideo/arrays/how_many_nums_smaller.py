class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # res = [0]*n
        # hash_map = {}
        # for num in nums:
        #     hash_map[num] = hash_map.get(num, 0) + 1

        # for i in range(n):
        #     for k, v in hash_map.items():
        #         if k < nums[i]:
        #             res[i] += v

        # return res
        temp = sorted(nums)
        hash_index = {}

        for i in range(n):
            if temp[i] not in hash_index:
                hash_index[temp[i]] = i

        res = []
        for num in nums:
            res.append(hash_index[num])
        return res






class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        freqMap = {}
        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1
        for num, freq in freqMap.items():
            if freq > n//2:
                res = max(res, num)
        return res

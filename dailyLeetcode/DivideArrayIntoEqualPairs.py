class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        num_pairs = 0
        for v in res.values():
            if v % 2 !=0 :
                return False
            num_pairs += v // 2
        return num_pairs == len(nums)/2
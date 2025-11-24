class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = 0
        for num in nums:
            curr = (curr << 1) + num
            if curr % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res

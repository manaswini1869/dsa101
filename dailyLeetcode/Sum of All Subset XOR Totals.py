import itertools
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def getSubsets(input_list):
            if not input_list:
                return [[]]
            first = input_list[0]
            last = input_list[1:]
            subs_without = getSubsets(last)
            subs_with = []
            for subset in subs_without:
                subs_with.append([first]+ subset)
            return subs_without + subs_with
        subsets = getSubsets(nums)
        res = 0
        for sub in subsets:
            sub_xor = 0
            if sub:
                for num in sub:
                    sub_xor ^= num
            res += sub_xor
        return res

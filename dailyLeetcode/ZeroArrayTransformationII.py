class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        difference = [0] * (len(nums) + 1)
        k = 0
        sum1 = 0
        for i in range(len(nums)):
            while sum1 + difference[i] < nums[i]:
                k += 1

                if (k > len(queries)):
                    return -1
                l, r, val = queries[k-1]

                if r >= i:
                    difference[max(l, i)] += val
                    difference[r + 1] -= val
            sum1 += difference[i]
        return k


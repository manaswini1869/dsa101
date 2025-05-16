class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum2 = 0
        zeroes1 = zeroes2 = 0

        for i in nums1:
            sum1 += i
            if i == 0:
                sum1 += 1
                zeroes1 += 1

        for j in nums2:
            sum2 += j
            if j == 0:
                sum2 += 1
                zeroes2 += 1
        print(sum1, sum2)
        if (zeroes1 == 0 and sum2 > sum1) or (zeroes2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m = len(nums1)
#         n = len(nums2)
#         nums = nums1 + nums2
#         nums.sort()
#         mid = (m+n) // 2
#         if (m+n) % 2 != 0:
#             return nums[mid]
#         else:
#             return (nums[mid-1]+nums[mid]) / 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        na = len(nums1)
        nb = len(nums2)
        n = na + nb
        # nums = nums1 + nums2
        # nums.sort()
        # mid = (m+n) // 2
        # if (m+n) % 2 != 0:
        #     return nums[mid]
        # else:
        #     return (nums[mid-1]+nums[mid]) / 2


        def helper(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]

            a_index, b_index = (a_start+a_end) // 2, (b_start+b_end) // 2
            a_value, b_value = nums1[a_index], nums2[b_index]

            if a_index + b_index < k:
                if a_value > b_value:
                    return helper(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return helper(k, a_index + 1, a_end, b_start, b_end)
            else:
                if a_value > b_value:
                    return helper(k, a_start, a_index-1, b_start, b_end)
                else:
                    return helper(k, a_start, a_end, b_start, b_index - 1)

        if n % 2:
            return helper(n // 2, 0, na - 1, 0, nb-1)
        else:
            return (
                helper(n // 2 - 1, 0, na - 1, 0, nb - 1)
                + helper(n // 2, 0, na - 1, 0, nb - 1)
            ) / 2



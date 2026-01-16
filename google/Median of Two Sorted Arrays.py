class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        l1, l2 = 0, 0
        prev = curr = 0

        for _ in range(n//2 + 1):
            prev = curr
            if l1 < n1 and (l2 >= n2 or nums1[l1] <= nums2[l2]):
                curr = nums1[l1]
                l1 += 1
            else:
                curr = nums2[l2]
                l2 += 1
        if n % 2 == 0:
            return (prev+curr) / 2
        else:
            return curr










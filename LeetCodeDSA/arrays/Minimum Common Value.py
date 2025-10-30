class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_com = float("inf")

        n1 = len(nums1)
        n2 = len(nums2)

        e1 = 0
        e2 = 0
        while e1 < n1 and e2 < n2:
            if nums1[e1] == nums2[e2]:
                return nums2[e2]
            elif nums2[e2] > nums1[e1]:
                e1 += 1
            else:
                e2 += 1


        return -1



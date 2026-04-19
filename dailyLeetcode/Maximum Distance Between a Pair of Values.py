class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1), len(nums2)
        i = 0
        for j in range(m):
            if nums1[i] > nums2[j]:
                i += 1
                if i >= n:
                    break
        return max(j - i, 0)

        # ans = 0
        # n, m = len(nums1), len(nums2)
        # for i in range(n):
        #     left, right = i, m-1
        #     idx = -1
        #     while left <= right:
        #         mid = (left+right) // 2
        #         if nums2[mid] < nums1[i]:
        #             idx = mid
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     if idx == -1:
        #         last = m - 1
        #     else:
        #         last = idx - 1

        #     if last >= i:
        #         ans = max(ans, last - i)
        

        # return ans

        # n, m = len(nums1), len(nums2)
        # ans = float("-inf")

        # for i in range(n):
        #     for j in range(i, m):
        #         if nums1[i] <= nums2[j]:
        #             ans = max(ans, j - i)

        # return 0 if ans == float("-inf") else ans


        
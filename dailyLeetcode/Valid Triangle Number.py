class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # brute force
        # res = 0
        # n = len(nums)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if (nums[i] + nums[j] > nums[k] and nums[j] + nums[k] > nums[i] and nums[i] + nums[k] > nums[j]):
        #                 res += 1

        # return res

        # binary search

        # res = 0
        # nums.sort()
        # n = len(nums)

        # def binarySearch(left, right, x):
        #     while right >= left and right < n:
        #         mid = (right + left) // 2
        #         if (nums[mid] >= x):
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        #     return left

        # for i in range(n-2):
        #     k = i + 2
        #     if nums[i] != 0:
        #         for j in range(i+1, n-1):
        #             k = binarySearch(k, n-1, nums[i] + nums[j])
        #             res += k - j - 1
        # return res

        # linear scan
        n = len(nums)
        nums.sort()
        res = 0

        for i in range(n-2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i+1, n-1):
                    while k < n and nums[i] + nums[j] > nums[k]:
                        k += 1
                    res += k - j - 1
        return res



class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if min(nums[i:j+1]) == minK and max(nums[i:j+1]) == maxK:
        #             count += 1
        # return count
        # left, right = 0, 0
        # while right < n and left < right:
        #     if nums[right] == minK and nums[left] == maxK:
        #         count += 1
        #         if right + 1 < n and nums[right + 1] < maxK:
        #             right += 1
        #         else:
        #             left += 1
        #     elif nums[left] == minK:
        #         right += 1
        #     elif nums[right] == maxK:
        #         left += 1
        #     else:
        #         right += 1
        #         left += 1
        # return count
        leftBound, maxPos, minPos = -1, -1, -1
        count = 0
        for idx, num in enumerate(nums):
            if nums[idx] < minK or nums[idx] > maxK:
                leftBound = idx
            if num == minK:
                minPos = idx
            if num == maxK:
                maxPos = idx
            count += max(0, min(minPos, maxPos) - leftBound)
        return count
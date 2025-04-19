class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n =  len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if lower <= nums[i] + nums[j] <= upper:
        #             result.append((i,j))
        # return len(result)
        nums.sort()
        count = 0
        for i in range(n):
            l = i+1
            r = n-1
            while l <= r:
                mid = (l+r) // 2
                if nums[i] + nums[mid] >= lower:
                    r = mid - 1
                else:
                    l = mid + 1
            left = l
            l = i+1
            r = n-1
            while l<=r:
                mid = (l+r) // 2
                if nums[i] + nums[mid] <= upper:
                    l = mid + 1
                else:
                    r = mid - 1
            right = r
            if right >= left:
                count += right - left + 1
        return count
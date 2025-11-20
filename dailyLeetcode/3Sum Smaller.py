class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        count = 0

        for i in range(n-2):
            j = i + 1
            k = n-1
            while j < k:
                init = nums[i] + nums[j] + nums[k]
                if init < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1

        return count


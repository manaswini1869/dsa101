from collections import Counter, defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        n = len(nums)
        count = 0
        count_max = 0
        # counte = defaultdict(int)
        # for i in range(n+1):
        #     for j in range(i+1,n+1):
        #         counte = Counter(nums[i:j])
        #         if counte[max_num] >= k:
        #             count += 1
        # return count
        left = 0
        for right in range(n):
            if nums[right] == max_num:
                count_max += 1
            while count_max >= k:
                count += (n - right)
                if nums[left] == max_num:
                    count_max -= 1
                left += 1

        return count
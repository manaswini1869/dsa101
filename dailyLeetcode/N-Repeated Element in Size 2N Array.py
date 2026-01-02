class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        two_n = len(nums)
        n = two_n // 2
        # heap = {}
        # for i in nums:
        #     heap[i] = heap.get(i, 0)+1
        # for k, v in heap.items():
        #     if v == n:
        #         return k
        nums.sort()
        for i in range(n-1):
            if nums[i+1] == nums[i]:
                return nums[i]



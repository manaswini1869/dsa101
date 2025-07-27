class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        arr = [nums[0]]
        for x in nums[1:]:
            if x != arr[-1]:
                arr.append(x)
        n = len(arr)
        for i in range(1, n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                res += 1
            elif arr[i-1] > arr[i] < arr[i+1]:
                res += 1
        return res
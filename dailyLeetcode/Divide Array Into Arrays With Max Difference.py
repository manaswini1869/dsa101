class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        num_div = n // 3
        res = []
        nums = sorted(nums)
        print(nums)
        for i in range(0, n, 3):
            arr1 = nums[i:i+3]
            for m in range(0, 3):
                for j in range(m+1, 3):
                    if arr1[j] - arr1[m] > k:
                        return []
            res.append(arr1)
        return res
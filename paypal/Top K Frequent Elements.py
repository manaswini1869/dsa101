class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        res = []
        n = len(nums)
        count = 1
        freq = []
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                print(count, nums[i])
                count += 1
            else:
                freq.append((count, nums[i-1]))
                count = 1
        freq.append((count, nums[-1]))
        freq.sort(reverse=True, key = lambda x: x[0])
        return [num for _, num in freq[:k]]
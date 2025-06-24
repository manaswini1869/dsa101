class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result_indices_set = set()
        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                start_range = max(0, i - k)
                end_range = min(n, i + k + 1)
                for j in range(start_range, end_range):
                    result_indices_set.add(j)
        return sorted(list(result_indices_set))
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        dist = float("-inf")
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        n = len(arrays)
        for i in range(1, n):
            dist = max(
                dist,
                arrays[i][-1] - min_val,
                max_val - arrays[i][0]
            )
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return dist



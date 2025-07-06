class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_map = defaultdict(int)
        n = len(arr)
        res = float('-inf')
        for i in range(n):
            freq_map[arr[i]] += 1

        for key, val in freq_map.items():
            if key == val:
                res = max(res, key)

        return res if res != float('-inf') else -1



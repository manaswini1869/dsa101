class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        min_diff = float("inf")
        output = defaultdict(list)
        n = len(arr)
        arr.sort()
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            min_diff = min(min_diff, diff)
            output[diff].append((arr[i-1], arr[i]))
        return list(output[min_diff])



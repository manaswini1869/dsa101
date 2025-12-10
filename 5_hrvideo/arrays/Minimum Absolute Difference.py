class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        res = []
        min_diff = float("inf")
        for i in range(n-1):
            curr_min_diff = abs( - arr[i] + arr[i+1])

            if curr_min_diff == min_diff:
                res.append([arr[i], arr[i+1]])
            elif curr_min_diff < min_diff:
                res = [[arr[i], arr[i+1]]]
                min_diff = curr_min_diff

        # for i in range(n-1):
        #     if abs(arr[i] - arr[i+1]) == min_diff:
        #         res.append([arr[i], arr[i+1]])

        return res





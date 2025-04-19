class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def back(start, arr, total):
            if len(arr) == k and sum(arr) == n:
                result.append(list(arr))
            if len(arr) > k and total > n:
                return
            for i in range(start,10):
                arr.append(i)
                back(i+1, arr, total+1)
                arr.pop()
        back(1, [], 0)
        return result
class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        n = len(arr)
        if n < 3:
            return 0
        res = float("-inf")
        for i in range(1, n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                left, right = i-1, i+1
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1

                res = max(res, right-left + 1)
        return res if res != float("-inf") else 0







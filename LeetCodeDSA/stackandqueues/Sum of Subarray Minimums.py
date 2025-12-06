# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:

#         MOD = 10**9 + 7
#         total = 0
#         n = len(arr)
#         stack = []

#         for i in range(n):
#             curr = arr[i]
#             total += curr
#             for j in range(i+1, n):
#                 curr = min(curr, arr[j])
#                 total += curr


#         return total % MOD


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10**9 + 7
        total = 0
        n = len(arr)
        stack = []

        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):

                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                total += (arr[mid] * ((mid - left) * (right - mid)))

            stack.append(i)

        return total % MOD



class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        mod = 10**9+7
        count = 0
        curr_sum = odds = evens = 0
        for i in range(n):
            curr_sum += arr[i]

            if curr_sum % 2: #odd
                count += 1 + evens
                odds += 1
            else:
                count += odds
                evens += 1

        return count % mod

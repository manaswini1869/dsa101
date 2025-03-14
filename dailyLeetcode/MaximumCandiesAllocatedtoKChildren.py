class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left, right = 1, max(candies)
        best = right
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                break
            serv = sum(c // mid for c in candies)
            if serv >= k:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best
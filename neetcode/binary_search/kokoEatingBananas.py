class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l<=r:
            mid = (l+r)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k


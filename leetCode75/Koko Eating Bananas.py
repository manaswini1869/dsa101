class Solution:
    def kokoEatingBanana(piles, h):
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right) // 2
            hours = 0
            for pile in piles:
                hours += pile / mid
            if hours < h:
                right = mid
            else:
                left = mid + 1
        return right
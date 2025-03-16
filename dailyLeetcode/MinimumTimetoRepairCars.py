class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        if cars == 0:
            return 0
        left, right = 1, max(ranks) * (cars**2)
        while left < right:
            t = (left + right) // 2
            n = sum(int(math.sqrt(t/r)) for r in ranks)
            if n >= cars:
                right = t
            else:
                left = t + 1
        return left
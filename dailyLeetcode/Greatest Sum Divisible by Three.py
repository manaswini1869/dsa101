class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        r1 = []
        r2 = []
        total = 0

        for num in nums:
            total += num
            if num % 3 == 1:
                r1.append(num)
            elif num % 3 == 2:
                r2.append(num)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            a = r1[0] if r1 else float('inf')
            b = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            return total - min(a, b)

        if total % 3 == 2:
            a = r2[0] if r2 else float('inf')
            b = sum(r1[:2]) if len(r1) >= 2 else float('inf')
            return total - min(a, b)

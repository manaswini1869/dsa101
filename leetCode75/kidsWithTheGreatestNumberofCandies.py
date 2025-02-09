class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxCandy = float('-inf')

        for i in candies:
            if i > maxCandy:
                maxCandy = i
        for i in candies:
            extraCandy = extraCandies + i
            if extraCandy >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res
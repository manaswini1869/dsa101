class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets.pop(i)
                    break
            else:
                count += 1
        return count
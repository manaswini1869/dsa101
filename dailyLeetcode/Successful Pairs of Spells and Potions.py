class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # n = len(spells)
        # m = len(potions)

        # res = []

        # for i in range(n):
        #     count = 0
        #     for j in range(m):
        #         if spells[i] * potions[j] >= success:
        #             count += 1
        #     res.append(count)

        # return res

        total_pairs = []
        potions.sort()
        n = len(potions)

        for spell in spells:
            left, right = 0, n - 1
            index = n

            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            count = n - index
            total_pairs.append(count)

        return total_pairs

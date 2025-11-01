class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(jewels)


        for st in stones:
            if st in jewels:
                count += 1

        return count


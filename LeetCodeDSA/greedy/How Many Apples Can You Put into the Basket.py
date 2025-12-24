class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        weight.sort()
        count = 0

        curr = 0
        n = len(weight)
        for i in range(n):
            if curr + weight[i] <= 5000:
                curr += weight[i]
                count += 1


        return count



















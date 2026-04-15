class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        if words[startIndex] == target:
            return 0

        n = len(words)
        dist = float("inf")

        for i in range(n):
            if words[i] == target:
                temp = min(abs(i-startIndex), n - abs(i - startIndex))
                dist = min(dist, temp)
        return dist if dist != float("inf") else -1

        
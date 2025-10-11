class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        if n < k:
            return max(energy)
        res = [0]*n

        for i in range(n-1, -1, -1):
            index = i + k
            if index < n:
                res[i] = energy[i] + res[index]
            else:
                res[i] = energy[i]

        return max(res)
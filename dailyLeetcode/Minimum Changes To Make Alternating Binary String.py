class Solution:
    def minOperations(self, s: str) -> int:

        ops1 = 0
        ops0 = 0
        n = len(s)

        for i, ch in enumerate(s):
            if ch != str(i%2):
                ops0 += 1
            if ch != str((i+1)%2):
                ops1 += 1
        return min(ops0, ops1)




        
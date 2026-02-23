class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        seen = set()
        n = len(s)
        left, right = 0, k
        while right <= n:
            seen.add(s[left:right])
            left += 1
            right += 1
        return len(seen) == 2**k

    # time complexity = O(n)
    # space complexity = O(2**k)




        
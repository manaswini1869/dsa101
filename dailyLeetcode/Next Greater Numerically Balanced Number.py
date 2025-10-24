class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n >= 10**6:
            return 1224444
        n += 1
        freq = Counter(str(n))
        if all(int(k) == v for k, v in freq.items()):
            return n

        return self.nextBeautifulNumber(n)



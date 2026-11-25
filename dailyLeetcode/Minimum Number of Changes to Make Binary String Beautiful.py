class Solution:
    def minChanges(self, s: str) -> int:

        n = len(s)

        sections = []
        for i in range(0, n, 2):
            sections.append(s[i:i+2])

        count = 0

        for sec in sections:
            count_one = sec.count("1")
            count_zero = sec.count("0")
            if (count_one != 0 or count_zero != 0):
                count += min(count_one, count_zero)

        return count

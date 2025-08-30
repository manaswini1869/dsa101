class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        res = set()

        n = len(phrases)

        for i in range(n):
            words = phrases[i].split()
            for j in range(n):
                if i == j:
                    continue
                words2 = phrases[j].split()

                if words[-1] == words2[0]:
                    merged = " ".join(words + words2[1:])
                    res.add(merged)

        return sorted(res)
class Solution:
    def vowelConsonantScore(self, s: str) -> int:

        vowels = set(['a','e','i','o','u'])

        score = 0
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i in vowels:
                    v += 1
                else:
                    c += 1
        if c > 0:
            score = math.floor(v / c)
        return score


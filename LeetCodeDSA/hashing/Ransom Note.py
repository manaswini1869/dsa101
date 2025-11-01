class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mapper = defaultdict(int)

        for m in magazine:
            mapper[m] += 1

        for r in ransomNote:
            if r not in mapper or mapper[r] == 0:
                return False
            else:
                mapper[r] -= 1

        return True

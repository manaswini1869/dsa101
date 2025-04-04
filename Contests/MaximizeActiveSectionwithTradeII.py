class Solution:
    def maxActiveforSubString(self, substring):
        max_active = sum([1 for char in substring if char == '1'])
        t = "1" + substring + "1"
        groups = []
        current = '1'
        count = 0
        for i in range(1, len(t)):
            if t[i] != current:
                groups.append((count, current))
                current = t[i]
                count = 1
            else:
                count += 1
        groups.append((count, current))
        max_group = 0
        for i in range(2, len(groups)):
            if groups[i-2][1] == '0' and groups[i][1] == '0':
                max_group = max(max_group, groups[i-2][0] + groups[i][0])
        return max(max_active, max_active + max_group)

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            print(query, s[query[0]: query[1] + 1])
            res.append(self.maxActiveforSubString(s[query[0]: query[1] + 1]))
        return res

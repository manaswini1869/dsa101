class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i) : chr(i) for i in range(ord('a'), ord('z')+1)}
        def find(x):
            if x != parent[x]:
                x = find(parent[x])
            return parent[x]

        def union(x, y):
            setx = find(x)
            sety = find(y)
            if setx < sety:
                parent[sety] = setx
            else:
                parent[setx] = sety
        for x, y in zip(s1, s2):
            union(x, y)

        res = ""
        for i in baseStr:
            res += find(i)

        return res
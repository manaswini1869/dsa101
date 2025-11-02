class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        mapper = defaultdict()
        ans = ""

        for src, dst in paths:
            mapper[src] = dst

        start = paths[0][0]

        while start in mapper:
            start = mapper[start]
        return start


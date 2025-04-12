class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birthMap = {}
        year = [float('inf'), 0]
        maxPopulation = 0
        res = 0
        for i in logs:
            birthMap[i[0]] = birthMap.get(i[0], 0) + 1
            birthMap[i[1]] = birthMap.get(i[1], 0) - 1
        birthMap = dict(sorted(birthMap.items()))
        print(birthMap)
        for yr, inc in birthMap.items():
            year[0] = yr
            year[1] = year[1] + inc
            if year[1] > maxPopulation:
                maxPopulation = year[1]
                res = year[0]
        return res
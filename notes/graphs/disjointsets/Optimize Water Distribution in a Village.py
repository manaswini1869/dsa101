class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size+1)]
        self.rank = [0] * (size+1)

    def find(self, house):
        while house != self.group[house]:
            house = self.find(self.group[house])
        return self.group[house]
    def union(self, house, pipe):
        set_house = self.find(house)
        set_pipe = self.find(pipe)
        if set_house == set_pipe:
            return False
        if self.rank[set_house] > self.rank[set_pipe]:
            self.group[set_pipe] = set_house
        elif self.rank[set_house] < self.rank[set_pipe]:
            self.group[set_house] = set_pipe
        else:
            self.group[set_house] = set_pipe
            self.rank[set_pipe] += 1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        edges = []
        for index, weight in enumerate(wells):
            edges.append((weight, 0, index+1))

        for house_1, house_2, cost in pipes:
            edges.append((cost, house_1, house_2))

        edges.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        total_cost = 0
        for cost, house_1, house_2 in edges:
            if uf.union(house_1, house_2):
                total_cost += cost
        return total_cost




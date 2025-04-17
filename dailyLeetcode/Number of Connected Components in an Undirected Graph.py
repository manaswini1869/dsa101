class Solution:
    def find(self, root, x):
        if x != root[x]:
            root[x] = self.find(root, root[x])
        return root[x]

    def combine(self, root, x, y):
        rootX = self.find(root, x)
        rootY = self.find(root, y)
        if rootX != rootY:
            root[rootY] = rootX

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        for x, y in edges:
            self.combine(root, x, y)
        return len(set(self.find(root, i) for i in range(n)))
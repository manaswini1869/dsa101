class Solution:
    def find(self, x, res):
        if x != res[x]:
            res[x] = self.find(res[x], res)
        return res[x]
    def union(self, x, y, res):
        rootx = self.find(x, res)
        rooty = self.find(y, res)
        if rootx != rooty:
            res[rooty] = rootx
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        res = [i for i in range(row)]
        for i in range(row):
            for j in range(i+1, row):
                if isConnected[i][j] == 1:
                    self.union(i, j, res)
        return len(set(self.find(i, res) for i in range(row)))




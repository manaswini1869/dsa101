class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        while len(res) < n:
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr == n or curr % 10 == 9:
                    curr = curr // 10
                curr += 1


        return res
        # def dfs(curr):
        #     if curr > n:
        #         return
        #     res.append(curr)
        #     curr *= 10
        #     for i in range(0,10):
        #         dfs(curr + i)
        # for i in range(1, 10):
        #     dfs(i)
        # return res
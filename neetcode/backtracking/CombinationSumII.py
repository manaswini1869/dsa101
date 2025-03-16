class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx-1]:
                    continue
                if total + candidates[idx] > target:
                    break
                cur.append(candidates[idx])
                dfs(idx + 1, cur, total + candidates[idx])
                cur.pop()
        dfs(0, [], 0)
        return res
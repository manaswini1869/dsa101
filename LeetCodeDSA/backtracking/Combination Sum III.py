class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        answer = []

        def backtrack(curr_sum, start, curr):
            if curr_sum == n and len(curr) == k:
                answer.append(curr[:])
                return
            if len(curr) > k or curr_sum > n:
                return

            for i in range(start, 10):
                curr.append(i)
                backtrack(curr_sum+i, i+1, curr)
                curr.pop()

        for i in range(1, 10):
            backtrack(i, i+1, [i])
        return answer





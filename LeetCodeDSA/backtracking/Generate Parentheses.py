class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []

        def backtrack(opne, close, curr):
            if opne == n and close == n:
                answer.append("".join(curr))
                return
            if opne < n:
                curr.append('(')
                backtrack(opne+1, close, curr)
                curr.pop()
            if close < opne:
                curr.append(')')
                backtrack(opne, close+1, curr)
                curr.pop()


        backtrack(0, 0, [])
        return answer










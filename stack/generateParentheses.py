class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        wellFormed = []
        res = []
        def backtrack(openc, closec):
            if openc == closec == n:
                res.append("".join(wellFormed))
                return
            if openc < n:
                wellFormed.append("(")
                backtrack(openc+1, closec)
                wellFormed.pop()
            if closec < openc:
                wellFormed.append(")")
                backtrack(openc, closec+1)
                wellFormed.pop()
        backtrack(0, 0)
        return res
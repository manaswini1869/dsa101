class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        if n == 1:
            return [i for i in range(10)]

        answer = []
        def backtrack(curr):
            if len(curr) == n:
                answer.append(int(curr))
                return

            for i in range(10):
                if abs(int(curr[-1])-i) == k:
                    backtrack(curr+str(i))


        for i in range(1, 10):
            backtrack(str(i))
        return answer






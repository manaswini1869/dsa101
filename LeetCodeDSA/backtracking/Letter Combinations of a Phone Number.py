class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        num_char_mapping = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        answer = []
        n = len(digits)

        def backtrack(idx, ch):
            if idx == n:
                answer.append(ch)
                return
            for nei in num_char_mapping[digits[idx]]:
                backtrack(idx+1, ch+nei)



        backtrack(0, '')



        return answer





class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_alpha = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def back(index, path):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            possible_letters = num_alpha[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                back(index+1, path)
                path.pop()
        result = []
        back(0, [])
        return result


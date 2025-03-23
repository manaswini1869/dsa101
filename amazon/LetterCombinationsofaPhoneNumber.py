class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_let_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        def backtrack(path, indx):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            possible_letter = num_let_map[int(digits[indx])]

            for letter in possible_letter:
                path.append(letter)
                backtrack(path, indx + 1)
                path.pop()

        combinations = []
        backtrack([], 0)
        return combinations
        # res = [""]
        # for dig in digits:
        #     tmp = []
        #     for r in res:
        #         for c in num_let_map[int(dig)]:
        #             tmp.append(r + c)
        #     res = tmp

        # return res
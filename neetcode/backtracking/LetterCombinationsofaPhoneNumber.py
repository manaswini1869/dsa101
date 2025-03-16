class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = [""]
        for digit in digits:
            tmp = []
            for s in res:
                for c in num_mapping[int(digit)]:
                    tmp.append(s + c)
            res = tmp
        return res


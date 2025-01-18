class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')':'(', '}':'{', ']':'['}
        p = []
        for i in s:
            if i in paren:
                if p and p[-1] == paren[i]:
                    p.pop()
                else:
                    return False
            else:
                p.append(i)
        if len(p) == 0:
            return True
        else:
            return False

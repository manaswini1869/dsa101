class Solution:
    def isValid(self, s: str) -> bool:
        brac_mapping = {')':'(', '}':'{', ']':'['}
        n = len(s)
        temp = []

        for i in range(n):
            if s[i] in brac_mapping.values():
                temp.append(s[i])
            else:
                if not temp or brac_mapping[s[i]] != temp.pop():
                    return False
        return len(temp) == 0

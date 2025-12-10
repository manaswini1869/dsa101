class Solution:
    def isValid(self, s: str) -> bool:

        mapper = {'}':'{', ']':'[', ')':'('}
        stack = []

        for ch in s:
            if ch in mapper.values():
                stack.append(ch)
            else:
                if not stack or mapper[ch] != stack.pop():
                    return False
        if stack:
            return False
        return True




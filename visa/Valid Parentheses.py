class Solution:
    def isValid(self, s: str) -> bool:

        valid_mapping = {')':'(', '}':'{', ']':'['}

        stack = []

        for i in s:
            if i == ')' or i == '}' or i == ']':
                if not stack:
                    return False
                else:
                    p = stack.pop()
                    if p != valid_mapping[i]:
                        return False
            else:
                stack.append(i)
        return len(stack) == 0


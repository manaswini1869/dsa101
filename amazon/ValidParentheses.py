class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', '}':'{',']':'['}
        brackets = []
        for brac in s:
            if brac in bracket_map.values():
                brackets.append(brac)
            else:
                if brackets and brackets[-1] == bracket_map[brac]:
                    brackets.pop()
                else:
                    return False
        return True if len(brackets) == 0 else False
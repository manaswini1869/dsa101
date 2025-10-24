class Solution:
    def isNumber(self, s: str) -> bool:

        valid = set(('-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', 'E', '.'))
        n = len(s)
        seen_digit = seen_expo = seen_dot = False
        isDigit = set(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
        isSign = set(('-', '+'))
        isExpo = set(('e', 'E'))
        isDeci = set(('.'))

        stack = []

        for i, ch in enumerate(s):
            if ch not in valid:
                return False
            elif ch in isDigit:
                seen_digit = True
            elif ch in isSign:
                if i > 0 and s[i-1] != "e" and s[i-1] != "E":
                    return False
            elif ch in isExpo:
                if seen_expo or not seen_digit:
                    return False
                seen_expo = True
                seen_digit = False
            elif ch in isDeci:
                if seen_dot or seen_expo:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit
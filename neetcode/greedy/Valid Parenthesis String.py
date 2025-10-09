class Solution:
    def checkValidString(self, s: str) -> bool:
        open_pa = []
        star = []
        n= len(s)
        for i in range(n):
            if s[i] == "(":
                open_pa.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if not star and not open_pa:
                    return False
                if open_pa:
                    open_pa.pop()
                else:
                    star.pop()

        while open_pa and star:
            if open_pa.pop() > star.pop():
                return False
        return not open_pa





class Solution:
    def isValid(self, s: str) -> bool:

        n = len(s)
        if not n:
            return True
        if n < 2:
            return False
        hash_map = {'(':')','{':'}','[':']'}
        stack = []
        for i in range(n):
            if s[i] in hash_map.values():
                if stack:
                    ch = hash_map[stack.pop()]
                    if ch != s[i]:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False




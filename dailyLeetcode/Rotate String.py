class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        slen, glen = len(s), len(goal)
        if slen != glen:
            return False

        return goal in (s + s)


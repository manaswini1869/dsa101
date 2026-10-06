class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        ans = 0
        arr = []

        for ch in s:
            if ch == '(':
                arr.append(ch)
            elif arr:
                arr.pop()
            else:
                ans += 1
        if arr:
            ans += len(arr)
        return ans
        


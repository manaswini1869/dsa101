class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        n = len(digits)
        if n < 3:
            return 0
        seen = set()

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if i == k or j == k:
                        continue
                    curr = digits[i]*100 + digits[j]*10 + digits[k]
                    if curr % 2 == 0:
                        seen.add(curr)
        return len(seen)
        



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]
        else:
            n = len(digits)
            rem = 1
            for i in range(n-1, -1, -1):
                s = digits[i] + rem
                digits[i] = s % 10
                rem = s // 10
            if rem:
                digits = [rem] + digits
            return digits




class Solution:
    def confusingNumber(self, n: int) -> bool:

        valid_number = {0:0, 1:1, 6:9, 8:8, 9:6}
        end = 0
        num = n
        while num:
            rem = num % 10
            if rem not in valid_number:
                return False
            rem = valid_number[rem]
            end = end*10 + rem
            num = num // 10
        if end == n:
            return False
        return True




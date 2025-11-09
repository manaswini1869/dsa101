class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        ops = 0
        while num1 != 0 or num2 != 0:
            if num1 == 0 or num2 == 0:
                break
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ops += 1

        return ops




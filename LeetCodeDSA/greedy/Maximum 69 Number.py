class Solution:
    def maximum69Number (self, num: int) -> int:

        final_max = num

        numbers = str(num)
        n = len(numbers)
        for i in range(n):
            if numbers[i] == '6':
                curr = numbers[:i] + '9'+ numbers[i+1:]
            else:
                curr = numbers[:i] + '6'+ numbers[i+1:]

            final_max = max(final_max, int(curr))


        return final_max














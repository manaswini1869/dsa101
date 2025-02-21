class Solution:
    def determine_partition(self, square_string, target, index=0, curr_sum=0):
        if index == len(square_string):
            return curr_sum == target
        num = 0
        for j in range(index, len(square_string)):
            num = num * 10 + int(square_string[j])
            if curr_sum + num > target:
                break
            if self.determine_partition(square_string, target, j+1, curr_sum+num):
                return True
        return False
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1,n+1):
            square_string = str(i*i)
            if self.determine_partition(square_string, i):
                result += (i*i)
        return result
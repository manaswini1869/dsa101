from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_map = defaultdict(list)
        for i in range(1, n+1):
            sum_digit = 0
            j = i
            while j:
                sum_digit += j % 10
                j = j // 10
            sum_map[sum_digit].append(i)
        res = 0
        largest_size = float('-inf')
        for val in sum_map.values():
            if len(val) >= largest_size:
                largest_size = len(val)
        for val in sum_map.values():
            if len(val) == largest_size:
                res += 1
        return res
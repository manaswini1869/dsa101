from sortedcontainers import SortedList
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)

        if k == 1:
            return nums[0]

        need = k - 1  # number of additional starts needed

        def move_left_to_right():
            nonlocal curr_sum
            x = left.pop()
            curr_sum -= x
            right.add(x)

        def move_right_to_left():
            nonlocal curr_sum
            x = right.pop(0)
            curr_sum += x
            left.add(x)

        end = min(n, dist + 2)

        left = SortedList(nums[1:end])
        right = SortedList()
        curr_sum = sum(left)

        while len(left) > need:
            move_left_to_right()

        ans = curr_sum

        for r in range(dist + 2, n):
            out = nums[r - dist - 1]
            if left and out <= left[-1]:
                left.remove(out)
                curr_sum -= out
            else:
                right.remove(out)

            x = nums[r]
            if left and x <= left[-1]:
                left.add(x)
                curr_sum += x
            else:
                right.add(x)

            while len(left) < need:
                move_right_to_left()
            while len(left) > need:
                move_left_to_right()

            ans = min(ans, curr_sum)

        return nums[0] + ans

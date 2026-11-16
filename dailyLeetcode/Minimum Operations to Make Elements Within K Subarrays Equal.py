from functools import lru_cache
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        # n = len(nums)

        # cost = [0]*n

        # for i in range(n-x+1):
        #     curr = sorted(nums[i:i+x])
        #     med = curr[(x-1)//2]
        #     cost[i] = sum(abs(med - num) for num in curr)

        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        count_tree = [0] * (m + 1)
        sum_tree = [0] * (m + 1)

        def update(tree, i, val):
            while i <= m:
                tree[i] += val
                i += i & -i

        def query(tree, i):
            res = 0
            while i > 0:
                res += tree[i]
                i -= i & -i
            return res

        def find_kth(k):
            idx = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= m and count_tree[nxt] < k:
                    idx = nxt
                    k -= count_tree[nxt]
                bit >>= 1

            return idx + 1

        cost = [0] * n
        window_sum = 0

        # Calculate cost for every sliding window
        for i in range(n):

            pos = bisect_left(vals, nums[i]) + 1

            update(count_tree, pos, 1)
            update(sum_tree, pos, nums[i])
            window_sum += nums[i]

            if i >= x:
                old = nums[i-x]
                old_pos = bisect_left(vals, old) + 1

                update(count_tree, old_pos, -1)
                update(sum_tree, old_pos, -old)
                window_sum -= old

            if i >= x-1:

                start = i-x+1

                med_idx = find_kth((x+1)//2)
                med = vals[med_idx-1]

                left_count = query(count_tree, med_idx)
                left_sum = query(sum_tree, med_idx)

                right_count = x - left_count
                right_sum = window_sum - left_sum

                cost[start] = (
                    med * left_count - left_sum
                    + right_sum - med * right_count
                )

        # @lru_cache(None)
        # def solve(count, idx): ## count = current number of subarrays with same elements; idx is the index in the array tracking the start of the sub array

        #     if count == k:
        #         return 0

        #     if idx + (k-count)*x > n:
        #         return float('inf')


        #     take = cost[idx] + solve(count + 1, idx + x)
        #     skip = solve(count, idx + 1)

        #     return min(take, skip)

        # return solve(0, 0)


        # Iterative DP instead of recursive memoization

        prev = [0] * (n + 1)

        for count in range(1, k + 1):

            curr = [float('inf')] * (n + 1)

            for idx in range(n + 1):

                # Skip current index
                curr[idx] = curr[idx-1] if idx > 0 else float('inf')

                # Take current window
                if idx >= x:
                    curr[idx] = min(
                        curr[idx],
                        cost[idx-x] + prev[idx-x]
                    )

            prev = curr

        return prev[n]

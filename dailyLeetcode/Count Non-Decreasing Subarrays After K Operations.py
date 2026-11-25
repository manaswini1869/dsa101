from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        a = nums[::-1]
        dq = deque()      # indices, values strictly decreasing
        S = 0             # sum of each window element's target (suffix max)
        total = 0         # plain sum of window
        L = 0
        ans = 0

        for R, x in enumerate(a):
            total += x
            cnt = 1       # elements whose max becomes x
            while dq and a[dq[-1]] <= x:
                j = dq.pop()
                prev = dq[-1] if dq else L - 1
                c = j - prev          # elements covered by j
                S -= a[j] * c
                cnt += c
            dq.append(R)
            S += x * cnt

            while S - total > k:
                S -= a[dq[0]]         # remove a[L]'s target
                total -= a[L]
                if dq[0] == L:
                    dq.popleft()
                L += 1

            ans += R - L + 1

        return ans
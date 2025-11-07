class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        n = len(stations)

        prefix = [stations[0]]

        for i in range(1, n):
            prefix.append(prefix[-1]+stations[i])

        initial = []
        for i in range(n):
            l, rr = i-r,i+r
            if l < 0:
                l = 0
            if rr >= n:
                rr = n-1
            if l == 0:
                initial.append(prefix[rr])
            else:
                initial.append(prefix[rr] - prefix[l-1])

        low = min(initial)
        high = max(initial) + k

        def can(target):
            add = [0] * (n + 1)
            extra_used = 0
            curr_add = 0

            for i in range(n):
                curr_add += add[i]
                curr_power = initial[i] + curr_add

                if curr_power < target:
                    need = target - curr_power
                    if extra_used + need > k:
                        return False

                    extra_used += need
                    curr_add += need
                    pos = min(n - 1, i + r)
                    end = pos + r + 1
                    if end < n:
                        add[end] -= need

            return True

        # binary search
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1




        return ans




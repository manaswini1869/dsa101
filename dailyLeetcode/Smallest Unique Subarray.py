class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        # seen = defaultdict(list)
        n = len(nums)
        base = 100003
        mod = (1<<61)-1

        prefix = [0]*(n+1)
        pwr = [1]*(n+1)

        for i in range(n):
            prefix[i+1] = (prefix[i]*base+nums[i]) % mod
            pwr[i+1] = (pwr[i]*base)%mod

        def window(st, length):
            return (prefix[st+length] - prefix[st]*pwr[length]) % mod

        def has(length):
            count = Counter(window(i, length) for i in range(n-length+1))
            return 1 in count.values()

        lo, hi = 1, n

        while lo < hi :

            mid = (lo+hi) // 2
            if has(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

        # for i in range(1, n+1):
        #     count = Count(tuple)

        # for i in range(n):
        #     curr = Counter(tuple(nums[j:j+i]) for j in range(n-i+1))
        #     if 1 in curr.values():
        #         return i # returning the subarray which appear only once
        # return n
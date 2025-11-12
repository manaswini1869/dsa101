class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if not n:
            return -1
        one_count = 0
        one_count = nums.count(1)
        if one_count:
            return n - one_count

        def get_gcd(a, b):
            if b == 0:
                return a
            else:
                return get_gcd(b, a%b)

        min_len = float("inf")
        for i in range(n):
            gcd = nums[i]
            for j in range(i+1, n):
                gcd = get_gcd(gcd, nums[j])
                if gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        if min_len == float("inf"):
            return -1

        return (min_len-1) + (n-1)



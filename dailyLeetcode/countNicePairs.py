class Solution:
    def rev(self, num: int) -> int:
        rev_num = 0
        while num > 0:
            digit = num % 10
            rev_num = rev_num * 10 + digit
            num = num // 10
        return rev_num
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9+7
        nice_pairs = 0
        count_map = defaultdict(int)
        for num in nums:
            rev_num = self.rev(num)
            diff = num - rev_num
            nice_pairs = (nice_pairs+count_map[diff])%MOD
            count_map[diff] += 1
        return nice_pairs

class Solution:
    def __inti__(self):
        self.memo = []
        self.nums = []

    def canJumPos(self, pos):
        if self.memo[pos] != -1:
            return self.memo[pos] == 1
        furthest_jump = min(pos + self.nums[pos], len(self.nums) - 1)
        for nxt in range(pos+1, furthest_jump+1):
            if self.canJumPos(nxt):
                return True
        self.memo[pos] = 0
        return False
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.memo = [-1] * len(nums)
        self.memo[-1] = 1
        return self.canJumPos(0)
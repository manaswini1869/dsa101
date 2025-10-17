class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        reminder_count = Counter(num % value for num in nums)

        mex = 0
        while reminder_count[mex % value] > 0:
            reminder_count[mex % value] -= 1
            mex += 1
        return mex


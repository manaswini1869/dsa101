class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_so_far = set()

        for num in nums:
            if num in nums_so_far:
                return True
            nums_so_far.add(num)

        return False


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sides = set(nums)
        n = len(sides)
        if (nums[0] + nums[1] > nums[2]) and (nums[0] + nums[2] > nums[1])  and (nums[2] + nums[1] > nums[0]):
            if n == 1:
                return "equilateral"
            elif n == 2:
                return "isosceles"
            elif n == 3:
                return "scalene"
            else:
                return "none"
        else:
            return "none"
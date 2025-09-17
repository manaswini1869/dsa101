class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x*y // gcd(x, y)

        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                g = gcd(stack[-1], stack[-2])
                if g > 1:
                    val = lcm(stack.pop(), stack.pop())
                    stack.append(val)
                else:
                    break

        return stack



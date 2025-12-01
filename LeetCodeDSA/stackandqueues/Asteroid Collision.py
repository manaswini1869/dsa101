class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for aste in asteroids:
            while stack and stack[-1] > 0 and aste < 0:
                if stack[-1] < -aste:
                    stack.pop()
                    continue
                elif stack[-1] == -aste:
                    stack.pop()
                break
            else:
                stack.append(aste)

        return stack


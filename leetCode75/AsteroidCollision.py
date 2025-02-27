class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(asteroid) > abs(top):
                    stack.pop()
                elif abs(asteroid) < abs(top):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack

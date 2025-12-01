class Solution:
    def robotWithString(self, s: str) -> str:
        paper = []
        robot = []
        n = len(s)
        min_char = [None]*n
        min_char[-1] = s[-1]

        for i in range(n-2, -1, -1):
            min_char[i] = min(s[i], min_char[i+1])

        for i, ch in enumerate(s):
            robot.append(ch)

            while robot and (i==n-1 or robot[-1] <= min_char[i+1]):
                paper.append(robot.pop())


        return "".join(paper)







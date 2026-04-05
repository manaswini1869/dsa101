class Solution:
    def judgeCircle(self, moves: str) -> bool:

        start = [0, 0]
        end = [0, 0]

        for move in moves:
            if move == 'U':
                end[1] += 1
            elif move == 'D':
                end[1] -= 1
            elif move == 'R':
                end[0] += 1
            else:
                end[0] -= 1
 
        return end[0] == start[0] and end[1] == start[1]



        
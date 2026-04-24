class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        n = len(moves)
        start = 0
        lc, rc, uc = 0, 0, 0
        for mv in moves:
            if mv == "L":
                lc += 1
            elif mv == "R":
                rc += 1
            else:
                uc += 1
        if lc > rc:
            return lc - rc + uc
        else:
            return rc - lc + uc
            
            


        
from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        
        # bfs
        n = len(board)
        cells = [None]*(n**2+1)
        columns = list(range(0, n))
        label = 1
        for row in range(n-1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1]*(n*n+1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()        
            for next in range(curr+1, min(curr+6, n**2)+1):
                row, col = cells[next]
                dest = (board[row][col] if board[row][col] != -1 else next)
                if dist[dest] == -1:
                    dist[dest] = dist[curr]+1
                    q.append(dest)
        return dist[n**2]
        # time complexity = O(n**2)
        # space complexity = O(n**2)
        
        
        
        
        
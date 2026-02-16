from collections import deque

class HitCounter:

    def __init__(self):
        # self.timestamp = []
        self.timestamp = deque()
        
    def hit(self, timestamp: int) -> None:
        self.timestamp.append(timestamp)  
         

    def getHits(self, timestamp: int) -> int:
        # starter = timestamp - 300 + 1
        # index = bisect_left(self.timestamp, starter)
        # return len(self.timestamp) - index

        while self.timestamp and self.timestamp[0] <= timestamp-300:
            self.timestamp.popleft()
        return len(self.timestamp)
        
    # time complexity = O(log n)
    # space complexity = O(n)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
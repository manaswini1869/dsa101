class NumberContainers:

    def __init__(self):
        self.noContainer = {}
        self.noIndices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.noContainer:
            prev = self.noContainer[index]
            if prev in self.noIndices:
                pass
        self.noContainer[index] = number
        if number not in self.noIndices:
            self.noIndices[number] = []
        heapq.heappush(self.noIndices[number], index)

    def find(self, number: int) -> int:
        if number not in self.noIndices or not self.noIndices[number]:
            return -1
        while self.noIndices[number] and self.noContainer[self.noIndices[number][0]] != number:
            heapq.heappop(self.noIndices[number])
        return self.noIndices[number][0] if self.noIndices[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# heapq is a heap queue algorithm (priority queue) implementation in Python. It provides a way to efficiently manage a collection of elements while keeping them sorted automatically.
#It maintains a binary heap (a tree-like structure).
# The smallest element is always at index 0.
# Adding (push) and removing (pop) elements are O(log n) operations.
# Retrieving the smallest element (heap[0]) is O(1)
# implementing min heap

class MinHeap:
    # initializing the min heap
    def __init__(self, heapSize):
        self.heapSize = heapSize
        self.minHeap = [0] * (heapSize + 1)
        self.realSize = 0

    # function to add element into the min heap
    def add(self, element):
        self.realSize += 1
        if self.realSize > self.heapSize:
            print("Added too many elements")
            self.realSize -= 1
            return
        self.minHeap[self.realSize] = element
        index = self.realSize
        parent = index // 2
        while (self.minHeap[index] < self.minHeap[parent] and index > 1):
            self.minHeap[parent], self.minHeap[index] = self.minHeap[index], self.minHeap[parent]
            index = parent
            parent = index // 2

    # function to look at the top element
    def peek(self):
        return self.minHeap[1]

    # function to remove the top element
    def pop(self):
        if self.realSize < 0:
            print("No elements in minHeap")
            return
        else:
            remove = self.minHeap[1]
            self.minHeap[1] = self.minHeap[self.realSize]
            self.realSize -= 1
            index = 1
            while (index <= self.realSize):
                left = index * 2
                right = index * 2 + 1
                if (self.minHeap[index] > self.minHeap[left] or self.minHeap[index] > self.minHeap[right]):
                    if self.minHeap[left] > self.minHeap[right]:
                        self.minHeap[right], self.minHeap[index] = self.minHeap[index], self.minHeap[right]
                        index = right
                    else:
                        self.minHeap[left], self.minHeap[index] = self.minHeap[index], self.minHeap[left]
                        index = left
                else:
                    break
            return remove

    # function to return the size of the element
    def size(self):
        return self.realSize

    def __str__(self):
        return str(self.minHeap[1: self.realSize+1])

if __name__ == "__main__":
    minHeap = MinHeap(5)
    minHeap.add(3)
    minHeap.add(1)
    minHeap.add(2)
    print(minHeap)
    print(minHeap.peek())
    print(minHeap.pop())
    print(minHeap.pop())
    print(minHeap.pop())
    minHeap.add(4)
    minHeap.add(5)
    print(minHeap)



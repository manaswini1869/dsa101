class MyQueue:

    def __init__(self):
        self.stackQ = []

    def push(self, x: int) -> None:
        self.stackQ.append(x)

    def pop(self) -> int:
        if len(self.stackQ) > 0:
            num = self.stackQ.pop(0)
            return num
        else:
            return -1

    def peek(self) -> int:
        if len(self.stackQ)> 0:
            print(self.stackQ)
            return self.stackQ[0]
        else:
            return -1

    def empty(self) -> bool:
        if len(self.stackQ) > 0:
            return False
        else:
            return True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
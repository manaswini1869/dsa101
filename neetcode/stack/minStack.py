class MinStack:

    def __init__(self):
        self.minVal = [] # stack to store the minimum value seen so far
        self.minStack = [] # stack to store the input values for the operations

    def push(self, val: int) -> None:
        self.minStack.append(val)
        val = min(val, self.minVal[-1] if self.minVal else val)
        self.minVal.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.minVal.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]



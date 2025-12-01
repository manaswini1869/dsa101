class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = val if not self.stack else min(self.stack[-1][1], val)
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.curr_min = float("inf")

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if val < self.curr_min:
#             self.curr_min = val

#     def pop(self) -> None:
#         val = self.stack.pop()
#         if val == self.curr_min:
#             self.curr_min = float("inf")
#             for num in self.stack:
#                 if num < self.curr_min:
#                     self.curr_min = num

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.curr_min



# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
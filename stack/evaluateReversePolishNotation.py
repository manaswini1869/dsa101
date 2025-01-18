class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []

        for i in tokens:
            if i == "+":
                numStack.append(numStack.pop() + numStack.pop())
            elif i == "-":
                a, b = numStack.pop(), numStack.pop()
                numStack.append(b - a)
            elif i == "*":
                numStack.append(numStack.pop() * numStack.pop())
            elif i == "/":
                a, b = numStack.pop(), numStack.pop()
                numStack.append(int(b / a))
            else:
                numStack.append(int(i))
        return numStack.pop()
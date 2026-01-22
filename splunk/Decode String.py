class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                curr_str = ""
                while stack and stack[-1] != '[':
                    curr_str = stack.pop() + curr_str
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(curr_str*num)
        return "".join(stack)









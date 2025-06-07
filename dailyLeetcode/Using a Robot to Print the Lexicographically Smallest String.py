class Solution:
    def robotWithString(self, s: str) -> str:
        char_counter = Counter(s)
        result = []
        stack = []
        min_char = 'a'
        for char in s:
            char_counter[char] -= 1
            while min_char <= 'z' and char_counter[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            stack.append(char)
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())
        return ''.join(result)


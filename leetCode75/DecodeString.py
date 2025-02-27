class Solution:
    def decodeString(self, s: str) -> str:
        decode_str = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                decode_str.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                prev_str, num = decode_str.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
        return current_str
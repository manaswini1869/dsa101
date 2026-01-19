class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:

        freq_map = defaultdict(int)

        for ch in s:
            freq_map[ch] += 1

        stack = []

        for ch in s:
            while stack and freq_map[stack[-1]] > 1 and ch < stack[-1]:
                freq_map[stack.pop()] -= 1
            stack.append(ch)
        while freq_map[stack[-1]] > 1:
            freq_map[stack.pop()] -= 1
        return "".join(stack)













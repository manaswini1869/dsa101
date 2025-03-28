class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left, right = 0, k
        sub_string_count = 0
        while right <= len(s):
            letters = set()
            repeated = False
            for i in s[left:right]:
                if i in letters:
                    repeated = True
                    break
                letters.add(i)
            if not repeated:
                sub_string_count += 1
            right += 1
            left += 1
        return sub_string_count


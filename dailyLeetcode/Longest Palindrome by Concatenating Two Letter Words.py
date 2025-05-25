class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counter = Counter(words)
        length = 0
        has_center = False

        for word in words:
            rev = word[::-1]
            if word != rev:
                if rev in word_counter:
                    pairs = min(word_counter[word], word_counter[rev])
                    length += pairs*4
                    word_counter[word] -= pairs
                    word_counter[rev] -= pairs
            else:
                pairs = word_counter[word] // 2
                length += pairs * 4
                word_counter[word] -= pairs * 2
                if word_counter[word] > 0:
                    has_center = True
        if has_center:
            length += 2
        return length
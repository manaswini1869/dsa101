from collections import defaultdict
from typing import List
import string

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        alpha_mapping = defaultdict(str)
        weight_mapping = defaultdict(int)
        for idx in range(26):
            alpha_mapping[idx] = chr(ord('z') - idx)
        for ch, val in zip(string.ascii_lowercase, weights):
            weight_mapping[ch] = val
        res = ""
        for word in words:
            curr = 0
            for ch in word:
                curr += weight_mapping[ch]
            curr %= 26
            res += alpha_mapping[curr]

        return res



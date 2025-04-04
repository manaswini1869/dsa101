from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurence = {char: i for i, char in enumerate(S)}
        left, right = 0, 0
        partitions = []

        for i, char in enumerate(S):
            right = max(last_occurence[char], right)
            if i == right:
                partitions.append(i - left + 1)
                left = i + 1
        return partitions
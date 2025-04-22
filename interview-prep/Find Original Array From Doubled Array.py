from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        freq = {}
        changed.sort()
        answer = []
        for num in changed:
            freq[num] = freq.get(num, 0) + 1
        # freq = Counter(nums)
        for num in changed:
            if freq.get(num, 0) == 0:
                continue
            if freq.get(2 * num, 0) == 0:
                return []
            freq[num] -= 1
            freq[2*num] -= 1
            answer.append(num)

        return answer
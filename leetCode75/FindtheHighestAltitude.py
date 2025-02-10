class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        init = 0
        max_alt = init
        for ga in gain:
            init += ga
            max_alt = max(max_alt, init)
        return max_alt

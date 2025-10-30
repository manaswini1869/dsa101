class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = curr_alt

        for ga in gain:
            curr_alt += ga
            max_alt = max(max_alt, curr_alt)

        return max_alt


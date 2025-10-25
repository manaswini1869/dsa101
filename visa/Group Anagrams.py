class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in freq:
                freq[sorted_str].append(s)
            else:
                freq[sorted_str].append(s)

        return list(freq.values())

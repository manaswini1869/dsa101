class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_group = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            hash_group[tuple(count)].append(s)

        return list(hash_group.values())



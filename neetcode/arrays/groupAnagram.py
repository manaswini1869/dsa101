class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagramRes = defaultdict(list)
        # for i in strs:
        #     resIndex = ''.join(sorted(i))
        #     anagramRes[resIndex].append(i)
        # return list(anagramRes.values())/
        anagraRes = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c) - ord('a')] += 1
            print(count)
            anagraRes[tuple(count)].append(i)
        return list(anagraRes.values())
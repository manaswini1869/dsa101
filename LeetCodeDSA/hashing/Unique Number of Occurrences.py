class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        mapper = defaultdict(int)

        for i in arr:
            mapper[i] += 1

        return len(set(mapper.values())) == len(mapper.values())


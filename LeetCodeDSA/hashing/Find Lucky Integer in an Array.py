class Solution:
    def findLucky(self, arr: List[int]) -> int:

        lucky = float("-inf")
        mapper = defaultdict(int)

        for i in arr:
            mapper[i] += 1

        for k, v in mapper.items():
            if k == v:
                lucky = max(lucky, k)

        return lucky if lucky != float("-inf") else -1


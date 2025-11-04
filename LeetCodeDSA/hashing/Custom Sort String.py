class Solution:
    def customSortString(self, order: str, s: str) -> str:

        mapper = defaultdict(int)
        for i in s:
            mapper[i] += 1

        result = ""
        n = len(order)

        for i in order:
            while i in mapper and mapper[i] > 0:
                result += i
                mapper[i] -= 1
            if mapper[i] == 0:
                del mapper[i]
        for k, v in mapper.items():
            result += k*v
        return result



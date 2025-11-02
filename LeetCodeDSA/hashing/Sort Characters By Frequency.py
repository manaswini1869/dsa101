class Solution:
    def frequencySort(self, s: str) -> str:

        # multiset and bucketsort

        mapper = defaultdict(int)
        for i in s:
            mapper[i] += 1

        max_freq = max(mapper.values())

        buckets = [[] for _ in range(max_freq + 1)]

        for ch, v in mapper.items():
            buckets[v].append(ch)

        ans = []

        for i in range(len(buckets)-1, 0, -1):
            for ch in buckets[i]:
                ans.append(ch*i)

        return "".join(ans)

        # mapper = defaultdict(int)
        # ans = ""
        # for i in s:
        #     mapper[i] += 1

        # sorted_mapper = sorted(mapper.items(), key=lambda x: x[1], reverse=True)

        # for k, v in sorted_mapper:
        #     ans += k*v

        # return ans



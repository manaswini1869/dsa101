class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        count = 0
        n = len(envelopes)
        sorted_env = sorted(envelopes, key=lambda item: (item[0], -item[1]))
        if n < 2:
            return n
        height = [h for _, h in sorted_env]
        lis = []
        for h in height:
            idx = bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)







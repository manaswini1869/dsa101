class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_sum = [0] * n
        left_candle = [-1] * n
        right_candle = [-1] * n

        plate_count = 0
        for i in range(n):
            if s[i] == '*':
                plate_count += 1
            prefix_sum[i] = plate_count

        last_candle = -1
        for i in range(n):
            if s[i] == '|':
                last_candle = i
            left_candle[i] = last_candle

        last_candle = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                last_candle = i
            right_candle[i] = last_candle

        res = []
        for l, r in queries:
            right_candle_idx = right_candle[l]
            left_candle_idx = left_candle[r]

            if right_candle_idx == -1 or left_candle_idx == -1 or right_candle_idx >= left_candle_idx:
                res.append(0)
            else:
                res.append(prefix_sum[left_candle_idx] - prefix_sum[right_candle_idx])
        return res
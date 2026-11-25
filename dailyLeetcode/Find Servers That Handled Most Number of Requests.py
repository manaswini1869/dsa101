class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        n = len(arrival)

        ans = []
        busy = []
        available = SortedList(range(k))
        server_count = [0]*k

        for i in range(n):
            arr, amt = arrival[i], load[i]
            while busy and busy[0][0] <= arr:
                t, s = heapq.heappop(busy)
                available.add(s)

            if not available:
                continue

            ser = i % k
            idx = available.bisect_left(ser)

            if idx == len(available):
                idx = 0

            s = available.pop(idx)
            server_count[s] += 1
            heapq.heappush(busy, (arr+amt, s))

        max_count = max(server_count)

        for j in range(k):
            if server_count[j] == max_count:
                ans.append(j)

        return ans

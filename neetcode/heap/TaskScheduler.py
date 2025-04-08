class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        max_heap = []
        tasks_order = deque()
        time = 0
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1
        for task, freq in freq_map.items():
            heapq.heappush(max_heap, -freq)
        while max_heap or tasks_order:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    tasks_order.append([cnt, time+n])
            if tasks_order and tasks_order[0][1] == time:
                heapq.heappush(max_heap, tasks_order.popleft()[0])
        return time
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # count = 0
        # task_completed = []
        # worker_done = []
        # for tidx, task in enumerate(tasks):
        #     for widx, worker in enumerate(workers):
        #         if worker >= task and (tidx, task) not in task_completed and (widx, worker) not in worker_done:
        #             count += 1
        #             worker_done.append((widx, worker))
        #             task_completed.append((tidx, task))
        #         elif pills:
        #             if worker + strength >= task and (tidx, task) not in task_completed and (widx, worker) not in worker_done:
        #                 pills -= 1
        #                 count += 1
        #                 worker_done.append((widx, worker))
        #                 task_completed.append((tidx, task))
        # return count
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        def check(mid):
            p = pills
            ws = SortedList(workers[m - mid:])
            for i in range(mid - 1, -1, -1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

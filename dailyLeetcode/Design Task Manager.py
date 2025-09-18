class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.highest = []
        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (userId, priority)
            self.highest.append((-priority, -taskId, userId))
        heapq.heapify(self.highest)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.highest, ((-priority, -taskId, userId)))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.tasks.get(taskId)
        self.tasks[taskId] = (userId, newPriority)
        heapq.heappush(self.highest, (-newPriority, -taskId, userId))


    def rmv(self, taskId: int) -> None:
        userId = self.tasks.get(taskId)[0]
        del self.tasks[taskId]


    def execTop(self) -> int:
        while self.highest:
            priority, taskId, userId = heapq.heappop(self.highest)
            tid, prio = -taskId, -priority
            if tid in self.tasks:
                uid, p = self.tasks[tid]
                if p == prio and uid == userId:
                    del self.tasks[tid]
                    return userId
        return -1




# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k]-1)

        return time

        # n = len(tickets)
        # tickets[k] *= -1

        # tickets = deque(tickets)
        # time = 0
        # while tickets:
        #     curr = tickets.popleft()
        #     time += 1
        #     if curr > 0:
        #         curr -= 1
        #     else:
        #         curr += 1
        #         if curr == 0:
        #             return time
        #     if curr != 0:
        #         tickets.append(curr)




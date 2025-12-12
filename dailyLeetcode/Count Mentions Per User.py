class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        mentions = [0]*numberOfUsers

        offline = [0]*numberOfUsers

        def get_event_sort_key(event):
            timestamp = int(event[1])

            if event[0] == "OFFLINE":
                priority = 0
            else:
                priority = 1
            return (timestamp, priority)
        events.sort(key=get_event_sort_key)
        for event in events:
            stat, time, id = event
            time = int(time)
            if stat == "OFFLINE":
                offline[int(id)] = time + 60
            else:
                ids = id.split()
                for i in ids:
                    if i == "ALL":
                        mentions = [k+1 for k in mentions]
                    elif i == "HERE":
                        for u in range(numberOfUsers):
                            if offline[u] <= time:
                                mentions[u] += 1
                    else:
                        mentions[int(i[2:])] += 1

        return mentions






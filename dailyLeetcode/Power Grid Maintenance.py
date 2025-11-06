class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        online = set()
        station_group = defaultdict(int)
        grid = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return

            online.add(station)
            station_group[station] = group_id
            heapq.heappush(grid[group_id], station)
            for nei in adj[station]:
                dfs(nei, group_id)


        for i in range(1, c+1):
            dfs(i, i)

        result = []

        for q_t, q_s in queries:
            if q_t == 1:
                if q_s in online:
                    result.append(q_s)
                else:
                    group_id = station_group[q_s]
                    gr = grid[group_id]
                    while gr and gr[0] not in online:
                        heapq.heappop(gr)
                    if gr:
                        result.append(gr[0])
                    else:
                        result.append(-1)

            else:
                online.discard(q_s)

        return result



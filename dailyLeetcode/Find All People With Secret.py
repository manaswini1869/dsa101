class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:



        meetings.sort(key=lambda x: x[2])
        secrets = set([0, firstPerson])

        time_map = {}

        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)


        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        for t in time_map.keys():
            visit = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t])


        # times = sorted(set(m[2] for m in meetings))

        # for time in times:
        #     meeting_matrix = defaultdict(list)
        #     for x, y, t in meetings:
        #         if t == time:
        #             meeting_matrix[x].append(y)
        #             meeting_matrix[y].append(x)

        #     q = deque([p for p in meeting_matrix if p in secrets])
        #     visited = set()
        #     while q:
        #         curr_person = q.popleft()
        #         if curr_person in visited:
        #             continue
        #         visited.add(curr_person)

        #         for i in meeting_matrix[curr_person]:
        #             if i not in visited:
        #                 q.append(i)
        #     secrets.update(visited)

        return list(secrets)










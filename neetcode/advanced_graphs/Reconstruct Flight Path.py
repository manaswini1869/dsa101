class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_matrix = {i:[] for i, _ in tickets}
        for _, dst in tickets:
            if dst not in adj_matrix:
                adj_matrix[dst] = []

        for sour, dest in tickets:
            adj_matrix[sour].append(dest)
        for src in adj_matrix:
            adj_matrix[src].sort()

        path = ["JFK"]


        def dfs(src):
            if len(path) == len(tickets) + 1:
                return True
            if src not in adj_matrix:
                return False

            for i, nei in enumerate(adj_matrix[src]):
                path.append(nei)
                adj_matrix[src].pop(i)

                if dfs(nei):
                    return True

                path.pop()
                adj_matrix[src].insert(i, nei)
            return False

        dfs("JFK")


        return path
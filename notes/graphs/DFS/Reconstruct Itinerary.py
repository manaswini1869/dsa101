class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for source, destination in sorted(tickets, reverse = True):
            adj_list[source].append(destination)
        result = []

        def dfs(node):
            while adj_list[node]:
                next_node = adj_list[node].pop()
                dfs(next_node)
            result.append(node)
        dfs('JFK')
        return result[::-1]
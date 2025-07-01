class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegree = Counter({c: 0 for word in words for c in word})

        # Constructing adj list
        for word, sec_wor in zip(words, words[1:]):
            for c, d in zip(word, sec_wor):
                if c != d:
                    if d not in adj[c]:
                        adj[c].append(d)
                        indegree[d] += 1
                    break
            else:
                if len(sec_wor) < len(word):
                    return ""

        # repeatedly pick of the indegree value with 0
        output = []
        queue = deque([c for c in indegree if indegree[c] == 0])

        while queue:
            c = queue.popleft()
            output.append(c)
            if c in adj:
                for nei in adj[c]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        queue.append(nei)
        if len(output) < len(indegree):
            return ""

        return "".join(output)


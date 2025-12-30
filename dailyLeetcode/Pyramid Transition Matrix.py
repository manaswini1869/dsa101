class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        n = len(bottom)

        adj = defaultdict(list)
        for a in allowed:
            adj[a[:2]].append(a[-1])

        def backtrack(idx, curr_str, curr_layer, next_row):
            if curr_layer == 1:
                return True
            if idx == curr_layer - 1:
                return backtrack(0, next_row, curr_layer-1, "")
            pair = curr_str[idx:idx+2]
            if pair not in adj:
                return False

            for nei in adj[pair]:
                if backtrack(idx+1, curr_str, curr_layer, next_row+nei):
                    return True
            return False

        return backtrack(0, bottom, n, "")











################################################################

# Try to do it yourself again


###################################################################

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)

        g = [[float('inf')] * (n+1) for _ in range(n+1)]

        for start in range(1, n+1):
            for end in range(start, n+1):
                sub = end - start + 1

                for d in range(1, sub):

                    if sub % d == 0:
                        changes_needed = 0
                        group = sub // d

                        for left_idx in range(sub):
                            group_pos = left_idx // d
                            offset = left_idx % d
                            right_idx = (group - 1 - group_pos) * d + offset

                            if left_idx >= right_idx:
                                break

                            if s[start-1+left_idx] != s[start-1+right_idx]:
                                changes_needed += 1

                        g[start][end] = min(g[start][end], changes_needed)

        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0

        for l in range(1, n+1):
            for parts in range(1, k+1):
                for prev_len in range(l):
                    if dp[prev_len][parts-1] != float('inf'):
                        dp[l][parts] = min(
                            dp[l][parts],
                            dp[prev_len][parts-1] + g[prev_len+1][l]
                        )

        return dp[n][k]
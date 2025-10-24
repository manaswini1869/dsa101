class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        from collections import defaultdict

        black = set((x, y) for x, y in coordinates)
        count_blocks = defaultdict(int)

        for x, y in black:
            for r, c in [(x-1,y-1), (x-1,y), (x,y-1), (x,y)]:
                if 0 <= r < m-1 and 0 <= c < n-1:
                    count_blocks[(r, c)] += 1

        ans = [0]*5
        for _, cnt in count_blocks.items():
            ans[cnt] += 1

        # we dont explicity calculate the number of 0 block, so calculate at the end
        total_blocks = (m-1) * (n-1)
        ans[0] = total_blocks - sum(ans[1:])
        return ans
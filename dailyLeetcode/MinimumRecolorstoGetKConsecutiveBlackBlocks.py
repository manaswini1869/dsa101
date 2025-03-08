class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j = 0, k-1
        res = float('inf')
        while j < len(blocks):
            counter = 0
            for block in blocks[i:j+1]:
                if block == 'W':
                    counter += 1
            if counter < res:
                res = counter
            i += 1
            j += 1
        return res


# class Solution:
#     def minimumRecolors(self, blocks: str, k: int) -> int:
#         current_w_count = sum(1 for i in range(k) if blocks[i] == 'W')
#         res = current_w_count
#         for i in range(1, len(blocks) - k + 1):
#             if blocks[i - 1] == 'W':
#                 current_w_count -= 1
#             if blocks[i + k - 1] == 'W':
#                 current_w_count += 1
#             res = min(res, current_w_count)

#         return res

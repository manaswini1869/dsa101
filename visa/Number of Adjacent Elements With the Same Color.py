class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        m = len(queries)
        same_adj = 0
        answer = [0] * m

        # def count(arr):
        #     res = 0
        #     for i in range(1, n):
        #         if arr[i] != 0 and arr[i-1] == arr[i]:
        #             res += 1
        #     return res


        for i in range(m):
            idx, color = queries[i]
            if idx > 0 and colors[idx] != 0 and colors[idx] == colors[idx-1]:
                same_adj -= 1
            if idx < n-1 and colors[idx] != 0 and colors[idx] == colors[idx+1]:
                same_adj -= 1

            colors[idx] = color
            # answer[i] = count(colors)

            if idx > 0 and colors[idx] != 0 and colors[idx] == colors[idx-1]:
                same_adj += 1
            if idx < n-1 and colors[idx] != 0 and colors[idx] == colors[idx+1]:
                same_adj += 1

            answer[i] = same_adj

        return answer



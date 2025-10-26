class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:


        n = len(capacity)

        if not capacity or n < 3:
            return 0

        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + capacity[i]

        count = 0

        visited = defaultdict(int)

        # for i in range(n):
        #     for j in range(i+2, n):
        #         if capacity[i] == capacity[j]:
        #             sum1 = prefix[j] - prefix[i+1]
        #             if sum1 == capacity[i]:
        #                 count += 1
        # return count


        for j in range(2, n):
            i = j - 2
            visited[(prefix[i + 1], capacity[i])] += 1
            target = (prefix[j] - capacity[j], capacity[j])
            count += visited[target]

            print(i, j, visited, target)

        return count



class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answers = [0] * (n-k+1)
        l = 0
        r = k
        while r < n+1:
            minHeap = []
            freq_map = {}
            for i in nums[l:r]:
                freq_map[i] = freq_map.get(i, 0) + 1

            if len(freq_map) < x:
                answers[l] = sum(nums[l:r])
            else:
                for key, value in freq_map.items():
                    heapq.heappush(minHeap, (-value, -key))
                for _ in range(x):
                    value, key = heapq.heappop(minHeap)
                    answers[l] += key*value
            l += 1
            r += 1
        return answers
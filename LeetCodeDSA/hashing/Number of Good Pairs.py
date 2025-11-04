class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mapper = defaultdict(int)
        n = len(nums)
        count = 0

        # for i in range(n):
        #     mapper[nums[i]].append(i)

        # for v in mapper.values():
        #     count += len(v) * (len(v) - 1) // 2

        # return count

        for num in nums:
            count += mapper[num]
            mapper[num] += 1
        return count


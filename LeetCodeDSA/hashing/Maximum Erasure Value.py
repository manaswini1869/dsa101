class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:


        start, end = 0, 0
        n = len(nums)

        mapper = defaultdict(int)
        prefix = [0]*(n+1)
        max_xum = 0

        for i in range(n):
            curr = nums[i]
            prefix[i+1] = prefix[i] + curr
            if curr in mapper:
                start = max(start, mapper[curr]+1)
            max_xum = max(max_xum, prefix[i+1] - prefix[start])
            mapper[nums[i]] = i

        return max_xum

        # left = 0
        # mapper = set()
        # curr = max_xum = 0
        # n = len(nums)

        # for right in range(n):
        #     while nums[right] in mapper:
        #         curr -= nums[left]
        #         mapper.remove(nums[left])
        #         left += 1
        #     curr += nums[right]
        #     mapper.add(nums[right])
        #     max_xum = max(max_xum, curr)

        # return max_xum

        # for i in range(n):
        #     curr = 0
        #     curr_set = set()
        #     for j in range(i, n):
        #         if nums[j] in curr_set:
        #             break
        #         curr += nums[j]
        #         curr_set.add(nums[j])
        #     max_sum = max(max_sum, curr)

        # return max_sum








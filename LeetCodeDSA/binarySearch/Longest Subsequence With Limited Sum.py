class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)
        total = sum(nums)

        answer = []
        nums.sort()

        prefix = []
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)

        for target in queries:
            left, right = 0, n-1
            res = 0
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] <= target:
                    res = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(res)





        return answer












class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:

        # time complexity = O(n)
        # space complexity = O(m) (m is the number of positive elements in the array)
        positives = [num for num in nums if num >= 0]
        if not positives:
            return nums
        m = len(positives)
        k %= m
        positives = positives[k:] + positives[:k]
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                nums[i] = positives[idx]
                idx += 1
        return nums

        # 
        # time complexity : O(n+k)
        # space complexity : O(n)
        # n = len(nums)

        # non_neg = deque()
        # ans = [float("inf")]*n

        # for i in range(n):
        #     if nums[i] < 0:
        #         ans[i] = nums[i]
        #     else:
        #         non_neg.append(nums[i])
        # if not non_neg:
        #     return ans
        # while k:
        #     curr = non_neg.popleft()
        #     non_neg.append(curr)
        #     k -= 1
        # for i in range(n):
        #     if ans[i] == float("inf"):
        #         ans[i] = non_neg.popleft()
        # return ans




        
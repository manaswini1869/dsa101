class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        answer[0] = 1
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if j != len(answer):
        #             prod *= nums[j]

        #     answer.append(prod)

        for i in range(1, n):
            answer[i] = nums[i-1] * answer[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] = right * answer[i]
            right *= nums[i]

        return answer
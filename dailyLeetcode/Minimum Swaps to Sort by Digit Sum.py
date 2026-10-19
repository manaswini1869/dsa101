class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        index_maps = {}

        n = len(nums)

        for i in range(n):
            curr_sum = self.getSum(nums[i])
            index_maps[nums[i]] = (i, curr_sum)
        
        sorted_nums = sorted(nums, key=lambda x: (index_maps[x][1], x))

        ans = 0

        target_index = {}
        for i in range(n):
            target_index[sorted_nums[i]] = i
        
        
        visit = [False]*n

        for i in range(n):
            if visit[i] or target_index[nums[i]] == i:
                continue
            
            cycle = 0
            j = i
            while not visit[j]:
                visit[j] = True
                j = target_index[nums[j]]
                cycle += 1
            
            ans += cycle - 1

        return ans
        

    def getSum(self, num):
        curr = 0
        while num:
            temp = num % 10
            curr += temp
            num //= 10

        return curr

        
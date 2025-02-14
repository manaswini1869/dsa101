# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         count_operations = 0
#         while len(nums) > 1:
#             nums.sort()
#             if nums[0] >= k:
#                 return count_operations
#             x, y = nums.pop(0), nums.pop(0)
#             insert_number = (min(x,y)*2 + max(x,y))
#             nums.append(insert_number)
#             count_operations += 1
#         return count_operations

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count_operations = 0
        heapq.heapify(nums)
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x*2+y)
            count_operations += 1
        return count_operations if nums[0] >= k else count_operations

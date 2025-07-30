class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # hash_map = defaultdict(list)
        # max_num = max(nums)
        # max_len = 1
        # curr_len = 1
        # n = len(nums)
        # for index, num in enumerate(nums):
        #     hash_map[num].append(index)
        # arr = hash_map[max_num]
        # print(arr)
        # for i in range(1, len(arr)):
        #     if arr[i] - 1 == arr[i-1]:
        #         curr_len += 1
        #     else:
        #         max_len = max(curr_len, max_len)
        #         curr_len = 1
        # max_len = max(curr_len, max_len)
        # return max_len
        max_val = ans = curr_str = 0

        for num in nums:
            if max_val < num:
                max_val = num
                ans = curr_str = 0

            if max_val == num:
                curr_str += 1
            else:
                curr_str = 0

            ans = max(curr_str, ans)

        return ans
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        # for num in nums:
        #     cnt = 0
        #     while num:
        #         num = num // 10
        #         cnt += 1
        #     if cnt % 2 == 0:
        #         count += 1
        # return count
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         count += 1
        # return count
        for num in nums:
            digi_count = int(math.floor(math.log10(num))) + 1
            if digi_count % 2 == 0:
                count += 1
        return count


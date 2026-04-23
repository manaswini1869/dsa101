class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        n = len(nums)
        arr = [0]*n
        hash_idx = defaultdict(list)

        for idx, val in enumerate(nums):
            hash_idx[val].append(idx)
        
        for idx in hash_idx.values():
            prefix = 0
            curr = sum(idx)

            for i, dx in enumerate(idx):
                left = i
                right = len(idx) - i - 1

                ls = prefix
                rs = curr - prefix - dx
                arr[dx] = (dx*left-ls)+(rs-dx*right)
                prefix += dx
        return arr


        # for i in range(n):
        #     if len(hash_idx[nums[i]]) > 0:
        #         temp = list(hash_idx[nums[i]])
        #         curr = 0
        #         for j in temp:
        #             curr += abs(i-j)
        #     arr[i] = curr

        # return arr



        
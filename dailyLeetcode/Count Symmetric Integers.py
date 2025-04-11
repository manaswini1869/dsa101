class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # count = 0
        # for i in range(low, high+1):
        #     if len(str(i)) < 2 or len(str(i)) % 2 != 0:
        #         continue
        #     n = len(str(i))
        #     str_i = list(str(i))
        #     n1, n2 = str_i[:n//2], str_i[n//2:]
        #     if sum(map(int, n1)) == sum(map(int,n2)):
        #         count += 1
        # return count
        res = 0
        for i in range(low, high+1):
            if i < 100 and i % 11 == 0:
                res += 1
            if 1000 <= i < 10000:
                left = i // 1000 + i % 1000 // 100
                right = i % 100 // 10 + i % 10

                if left == right:
                    res += 1
        return res
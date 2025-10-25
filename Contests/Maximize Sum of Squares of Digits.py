class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        ans = []

        #9 * 2 < 3 (18 < 3)
        if 9 * num < sum:
            return ""
        # num = 2
        for _ in range(num):
            for i in range(9, -1, -1): #(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
                if sum - i >= 0 and sum - i <= 9 * (num - 1): # (3 - 3)>=0 and (3 - 3)<= 9*1
                    ans.append(str(i))
                    sum -= i
                    break
            num -= 1
        return "".join(ans)


        # starter = 1
        # while num > 1:
        #     starter *= 10
        #     num -= 1

        # res = float("-inf")

        # for i in range(starter, starter*10):
        #     tmp = i
        #     curr = 0
        #     score = 0
        #     while tmp:
        #         remp = tmp % 10
        #         curr += remp
        #         score += remp * remp
        #         tmp //= 10
        #     if curr == sum:
        #         res = max(res, i)
        # return str(res) if res != float("-inf") else ""




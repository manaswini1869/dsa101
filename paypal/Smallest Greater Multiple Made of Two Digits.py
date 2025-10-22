class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        # if not digit1 and not digit2:
        #     return -1
        # applicable = {digit1, digit2}
        # limit = 2**31 - 1

        # def check(num):
        #     if num == 0:
        #         return 0 in applicable
        #     while num:
        #         if num % 10 not in applicable:
        #             return False
        #         num //= 10
        #     return True

        # res = k
        # while True:
        #     res += k  # next multiple greater than k
        #     if res > limit:
        #         return -1
        #     if check(res):
        #         return res

        mi = min(digit1, digit2)
        ma = max(digit1, digit2)
        q = deque([mi, ma] if mi != ma else [ma])

        while q:
            cur = q.popleft()
            if cur == 0 or cur > 2 ** 31 -1:
                continue
            if cur > k and cur % k == 0:
                return cur
            q.append(cur*10 + mi)
            if mi != ma:
                q.append(cur*10 + ma)
        return -1
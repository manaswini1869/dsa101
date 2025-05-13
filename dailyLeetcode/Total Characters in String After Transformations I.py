class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        # final_s = list(s)
        # MOD = 10**9 + 7
        # while t > 0:
        #     s = ""
        #     for letter in final_s:
        #         if letter == 'z':
        #             new_letter = 'ab'
        #         else:
        #             new_letter = chr(ord(letter) + 1)
        #         s += new_letter
        #     t -= 1
        #     final_s = list(s)
        # return len(final_s) % MOD
        dp = [0] * 26
        for letter in s:
            dp[ord(letter) - ord('a')] += 1
        while t > 0:
            new_count = [0] * 26
            for i in range(26):
                if dp[i] == 0:
                    continue
                if i == 25:
                    new_count[0] = (new_count[0] + dp[i]) % MOD
                    new_count[1] = (new_count[1] + dp[i]) % MOD
                else:
                    new_count[i+1] = (new_count[i+1] + dp[i]) % MOD
            dp = new_count
            t -= 1
        return sum(dp) % MOD


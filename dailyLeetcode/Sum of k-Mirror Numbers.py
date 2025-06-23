class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(num: int, k: int) -> str:
            result = ''
            while num > 0:
                result = str(num % k) + result
                num //= k
            return result

        count = 0
        total = 0
        length = 1
        while count < n:
            for root in range(10 ** ((length - 1) // 2), 10 ** ((length + 1) // 2)):
                s = str(root)
                if length % 2 == 0:
                    pal_str = s + s[::-1]
                else:
                    pal_str = s + s[-2::-1]
                pal_num = int(pal_str)

                if is_palindrome(to_base_k(pal_num, k)):
                    total += pal_num
                    count += 1
                    if count == n:
                        return total
            length += 1

        return total
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # allowed_letters = ['a', 'b', 'c']

        # def generate_happy_strings(current_str, length):
        #     if length == n:
        #         yield current_str
        #         return
        #     for letter in allowed_letters:
        #         if not current_str or current_str[-1] != letter:
        #             yield from generate_happy_strings(current_str + letter, length+1)

        # happy_string_gen = generate_happy_strings('', 0)

        # for _ in range(k-1):
        #     next(happy_string_gen, None)
        # return next(happy_string_gen, "")/

        allowed_letters = ['a', 'b', 'c']

        current_strings = ['a', 'b', 'c']

        for _ in range(1, n):
            next_string = []
            for s in current_strings:
                for letter in allowed_letters:
                    if s[-1] != letter:
                        next_string.append(s+letter)
            current_strings = next_string
        if k > len(current_strings):
            return ""
        return current_strings[k-1]
class Solution:
    def clearStars(self, s: str) -> str:
        g = defaultdict(list)
        n = len(s)
        rem = [False]*n
        for i, char in enumerate(s):
            if s[i] == '*':
                rem[i] = True
                for alpha in ascii_lowercase:
                    if g[alpha]:
                        rem[g[alpha].pop()] = True
                        break

            else:
                g[char].append(i)
        print(g)
        return ''.join(char for i, char in enumerate(s) if not rem[i])
#         stack = []
#         for char in s:
#             if char == '*':
#                 if stack:
#                     min_index = 0
#                     for i in range(1, len(stack)):
#                         if stack[i] <= stack[min_index]:
#                             min_index = i
#                     stack.pop(min_index)
#             else:
#                 stack.append(char)
#         return ''.join(stack)


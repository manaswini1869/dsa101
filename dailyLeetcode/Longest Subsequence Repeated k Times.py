class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        def is_subsequence(st):
            target = st * k
            it = iter(s)
            return all(c in it for c in target)

        # 1. Count the characters
        s_char_map = defaultdict(int)
        for i in s:
            s_char_map[i] += 1

        # 2. Extract hot characters
        hot_chars = sorted([char for char, count in s_char_map.items() if count >= k])

        ans = ""
        queue = deque([""])

        while queue:

            node = queue.popleft()

            for char in hot_chars:
                nxt = node + char

                if is_subsequence(nxt):
                    ans = nxt

                    queue.append(nxt)


        return ans
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        seen = set(wordList)
        if endWord not in seen:
            return 0

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        poss = 'abcdefghijklmnopqrstuvwxyz'

        while q:
            curr_word, curr_step = q.popleft()
            if curr_word == endWord:
                return curr_step
            for i in range(len(curr_word)):
                for j in poss:
                    if j == curr_word[i]:
                        continue
                    maybe = curr_word[:i]+j+curr_word[i+1:]
                    if maybe in seen and maybe not in visited:
                        q.append((maybe, curr_step+1))
                        visited.add(maybe)



        return 0









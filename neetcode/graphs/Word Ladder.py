class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        res = 1
        word_patterns = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                word_patterns[pattern].append(word)

        q = deque([beginWord])
        visit = set([beginWord])

        while q:
            for i in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return res
                for j in range(len(curr_word)):
                    pattern = curr_word[:j] + "*" + curr_word[j+1:]
                    for nei in word_patterns[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        return 0
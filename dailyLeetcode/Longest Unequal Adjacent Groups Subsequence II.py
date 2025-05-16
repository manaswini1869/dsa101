class Solution:
    def hamming_distance(self, s1, s2):
        ham_dist = 0
        if len(s1) != len(s2):
            return 2
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ham_dist += 1
        return ham_dist

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        lengths = [1] * n
        previous_index = [-1] * n
        max_length = 1

        for i, current_group in enumerate(groups):
            for j, prev_group in enumerate(groups[:i]):
                if (current_group != prev_group and lengths[i] < lengths[j] + 1 and self.hamming_distance(words[i], words[j]) == 1):
                    lengths[i] = lengths[j] + 1
                    previous_index[i] = j
                    max_length = max(lengths[i], max_length)
        longest_subseq = []
        for i in range(n):
            if lengths[i] == max_length:
                j = i
                while j >= 0:
                    longest_subseq.append(words[j])
                    j = previous_index[j]
                break
        return longest_subseq[::-1]

#         prev_group = 0
#         res = [words[prev_group]]

#         for i in range(1, n):
#             if groups[i] == groups[prev_group]:
#                 continue
#             if len(words[prev_group]) != len(words[i]):
#                 continue

#             if self.hamming_distance(words[prev_group], words[i]) != 1:
#                 continue

#             prev_group = i
#             res.append(words[prev_group])
#         return res


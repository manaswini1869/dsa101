class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index_mapping = defaultdict(list)

        n = len(s)
        for i in range(n):
            index_mapping[s[i]].append(i)


        total = 0

        for word in words:
            prev = -1
            found = True

            for ch in word:
                if ch not in index_mapping:
                    found = False
                    break
                indexes = index_mapping[ch]
                # found_next = False
                # for idx in indexes:
                #     if idx > prev:
                #         prev = idx
                #         found_next = True
                #         break

                # if not found_next:
                #     found = False
                #     break

                idx_pos = bisect.bisect_right(indexes, prev)

                if idx_pos == len(indexes):
                    found = False
                    break
                prev = indexes[idx_pos]

            if found:
                total += 1

        return total

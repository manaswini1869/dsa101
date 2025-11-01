class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapper = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

        for txt in text:
            if txt in mapper:
                mapper[txt] += 1

        count = 0

        if 0 in mapper.values():
            return count
        if mapper['l'] < 2 or mapper['o'] < 2:
            return count

        l_count = mapper['l']
        o_count = mapper['o']

        poss = min(l_count, o_count)

        poss //= 2

        poss_min = min(mapper.values())

        if poss > poss_min:
            return poss_min
        else:
            return poss


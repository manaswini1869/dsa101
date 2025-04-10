class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def cal(xrange, ssuffix, limit):
            if len(xrange) < len(ssuffix):
                return 0
            if len(xrange) == len(ssuffix):
                return 0 if xrange < ssuffix else 1
            count = 0
            plen = len(xrange) - len(ssuffix)
            sufx = xrange[plen:]
            for i in range(plen):
                if int(xrange[i]) > limit:
                    count = count + (limit + 1) ** (plen - i)
                    return count
                count = count + int(xrange[i]) * (limit+1) ** (plen - i - 1)
            if sufx >= s:
                count = count + 1
            return count
        return cal(str(finish), s, limit) - cal(str(start-1), s, limit)
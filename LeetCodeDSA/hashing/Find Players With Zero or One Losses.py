class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        losser = defaultdict(int)

        for w, l in matches:
            winner.add(w)
            losser[l] += 1

        res = [[]]*2
        for k, v in losser.items():
            if k in winner:
                winner.remove(k)
            if v == 1:
                res[1].append(k)
        res[0] = sorted(list(winner))
        res[1] = sorted(res[1])

        return res



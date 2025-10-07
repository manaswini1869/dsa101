class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        sunny = []
        rainy = {}
        ans = [-1]*n

        for day, lake in enumerate(rains):
            if lake > 0:
                if lake in rainy:
                    sunny_day = -1
                    sunny.sort()
                    for i in range(len(sunny)):
                        if sunny[i] > rainy[lake]:
                            sunny_day = i
                            break
                    if sunny_day == -1:
                        return []
                    dry_day = sunny[i]
                    del sunny[i]
                    ans[dry_day] = lake
                rainy[lake] = day
            else:
                sunny.append(day)
                ans[day] = 1
        return ans

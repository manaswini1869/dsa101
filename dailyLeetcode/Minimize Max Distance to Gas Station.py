class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        left, right = 0, 10**8
        n = len(stations)

        def check(x):
            needed_stations = 0
            for i in range(n-1):
                needed_stations += int((stations[i+1] - stations[i]) / x)

            return needed_stations <= k

        while right - left > 10**-6:
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid

        return left




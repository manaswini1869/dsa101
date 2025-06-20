class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # NE, NW, SE, SW

        def cal(prim, seco) -> int:
            max_dist = 0
            curr_dist = 0
            wron_cnt = 0

            for char in s:
                if char == prim or char == seco:
                    curr_dist += 1
                elif wron_cnt < k:
                    curr_dist += 1
                    wron_cnt += 1
                else:
                    curr_dist -= 1

                max_dist = max(max_dist, curr_dist)

            return max_dist


        distance_ne = cal('N', 'E')
        distance_nw = cal('N', 'W')
        distance_se = cal('S', 'E')
        distance_sw = cal('S', 'W')

        return max(distance_ne, distance_nw, distance_se, distance_sw)

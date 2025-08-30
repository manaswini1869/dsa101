class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = {}

        max_area = 0
        max_dia = 0

        for l, w in dimensions:
            curr_area = l * w
            curr_diagonal = math.sqrt(l**2 + w**2)

            if curr_diagonal > max_dia:
                max_area = curr_area
                max_dia = curr_diagonal

            elif curr_diagonal == max_dia:
                max_area = max(max_area, curr_area)

        return max_area
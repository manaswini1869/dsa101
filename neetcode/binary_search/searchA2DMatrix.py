class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, h = 0, len(row) - 1
            if (target>=row[l]) or (target<=row[h]):
                while l<=h:
                    mid = (l+h) // 2
                    if row[mid] == target:
                        return True
                    elif target < row[mid]:
                        h = mid - 1
                    else:
                        l = mid + 1
        return False
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:

        count = 0

        arr2.sort()
        n = len(arr2)
        for num1 in arr1:
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2

                target = abs(num1 - arr2[mid])

                if target > d:
                    if arr2[mid] < num1:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    break
            if left > right and (left >= n or right < 0):
                count += 1
            elif left > right and abs(num1 - arr2[max(0, min(left, n-1))]) > d:
                count += 1
        return count

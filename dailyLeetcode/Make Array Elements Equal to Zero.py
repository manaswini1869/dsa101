class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        dirc = 1 # direction > 0 right else left
        no_valid = 0
        n = len(nums)

        def proc(arr, dirc, curr):
            nonlocal no_valid
            while 0 <= curr < n:
                if arr[curr] == 0:
                    if dirc > 0:
                        curr += 1
                    else:
                        curr -= 1
                else:
                    arr[curr] -= 1
                    dirc = dirc * -1
                    if dirc > 0:
                        curr += 1
                    else:
                        curr -= 1
            if set(arr) == {0}:
                no_valid += 1

        for i in range(n):
            if nums[i] == 0:
                proc(nums[:], 1, i)
                proc(nums[:], -1, i)


        return no_valid


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # resList = nums1 + nums2
        # resList.sort()
        # if len(resList) % 2 != 0:
        #     return resList[len(resList)//2]
        # else:
        #     m = len(resList) // 2
        #     return (resList[m]+resList[m-1]) / 2
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2
        if len(b) < len(a):
            b, a = nums1, nums2
        l, r = 0, len(a) - 1
        while True:
            ma = (l+r) // 2
            mb = half - ma - 2

            aleft = a[ma] if ma >= 0 else float('-infinity')
            aright = a[ma+1] if (ma+1) < len(a) else float('infinity')
            bleft = b[mb] if mb >= 0 else float('-infinity')
            bright = b[mb+1] if (mb+1) < len(b) else float('infinity')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = ma - 1
            else:
                l = ma+1
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # res = []
        # n1, n2 = len(nums1), len(nums2)
        # for i in range(n1):
        #     for j in range(n2):
        #         res.append(nums1[i] * nums2[j])
        # return sorted(res)[k-1]
        def separate(nums):
            a1 = []
            a2 = []
            for num in nums:
                if num < 0:
                    a1.append(-num)
                else:
                    a2.append(num)
            a1.reverse()
            return a1, a2

        def numProductNotGreaterThan(A, B, m):
            count = 0
            j = len(B) - 1
            for a in A:
                while j >= 0 and a * B[j] > m:
                    j -= 1
                count += j+1
            return count

        A1, A2 = separate(nums1) # A1 neg
        B1, B2 = separate(nums2) # B1 neg

        # negative product count = negCount
        negCount = len(A1) * len(B2) + len(B1) * len(A2)
        sign = 1
        if k > negCount:
            k -= negCount
        else:
            k = negCount - k + 1
            sign = -1
            B1, B2 = B2, B1 # neg become pos, pos become neg

        l = 0
        r = 1e10

        while l < r:
            mid = (l+r) // 2
            if numProductNotGreaterThan(A1, B1, mid) + numProductNotGreaterThan(A2, B2, mid) >= k:
                r = mid
            else:
                l = mid + 1
        return int(sign * l)


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        v = nums2[-1]

        n = len(nums1)

        ans = 0

        last = float("inf")



        for a, b in zip(nums1, nums2):
            print(a, b)
            ans += abs(a - b)
            if a <= v <= b or b <= v <= a:
                last = 0
            last = min(last, abs(a-v), abs(b-v))

        return ans + last + 1




        # n = len(nums1)
        # ch = 0
        # min_diff = float("inf")
        # for i in range(n):
        #     if nums1[i] == nums2[-1]:
        #         ch = i
        #     else:
        #         diff = abs(nums1[i] - nums2[-1])
        #         if diff <= min_diff:
        #             ch = i
        #             min_diff = diff

        # arr = nums1[:]
        # arr.append(nums1[ch])
        # print(arr)
        # ops = 1
        # n += 1

        # # for i in range(n):
        # #     if nums1[i] == nums2[i]:
        # #         continue
        # #     elif nums1[i] > nums2[i]:
        # #         while nums1[i] != nums2[i]:
        # #             ops += 1
        # #             nums1[i] -= 1
        # #     else:
        # #         while nums1[i] != nums2[i]:
        # #             ops += 1
        # #             nums1[i] += 1

        # for i in range(n):
        #     if arr[i] != nums2[i]:
        #         ops += abs(arr[i] - nums2[i])
        #         arr[i] = nums2[i]
        # return ops



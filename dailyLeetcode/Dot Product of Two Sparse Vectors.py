class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = nums


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v2 = vec.data

        prod = 0
        for a, b in zip(self.data, v2):
            prod += (a*b)

        return prod


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
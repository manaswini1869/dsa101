class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        ans = []

        hash_map = defaultdict(list)
        small = float("inf")
        for num in arr:
            c = num.bit_count()
            hash_map[c].append(num)
            small = min(small, c)

        for key in sorted(hash_map.keys()):
            ans.extend(sorted(hash_map[key]))

        return ans

        # time complexity : O(nlogn)
        # space complexity : O(n)
        




        
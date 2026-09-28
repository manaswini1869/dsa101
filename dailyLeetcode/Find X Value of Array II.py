class Node:
    def __init__(self, k):
        self.remain = [0] * k
        self.prod = 1


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]

        self.build(nums, 0, 0, self.n - 1)

    # Updates nums[i] to val
    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)

    # Returns result of range query nums[i..j]
    def query(self, i, j):
        return self._query(0, 0, self.n - 1, i, j)

    def build(self, nums, cur, left, right):
        if left == right:
            self.tree[cur].remain[nums[left]] = 1
            self.tree[cur].prod = nums[left]
            return

        mid = (left + right) // 2

        self.build(nums, 2 * cur + 1, left, mid)
        self.build(nums, 2 * cur + 2, mid + 1, right)

        self.tree[cur] = self.merge(
            self.tree[2 * cur + 1],
            self.tree[2 * cur + 2]
        )

    def _update(self, tree_index, lo, hi, i, val):
        if lo == hi:
            self.tree[tree_index].remain = [0] * self.k
            self.tree[tree_index].remain[val] = 1
            self.tree[tree_index].prod = val
            return

        mid = (lo + hi) // 2

        if i <= mid:
            self._update(
                2 * tree_index + 1,
                lo,
                mid,
                i,
                val
            )
        else:
            self._update(
                2 * tree_index + 2,
                mid + 1,
                hi,
                i,
                val
            )

        self.tree[tree_index] = self.merge(
            self.tree[2 * tree_index + 1],
            self.tree[2 * tree_index + 2]
        )

    def _query(self, tree_index, lo, hi, i, j):
        # Completely inside
        if i <= lo and hi <= j:
            return self.tree[tree_index]

        # Completely outside
        if j < lo or hi < i:
            return Node(self.k)

        mid = (lo + hi) // 2

        left = self._query(
            2 * tree_index + 1,
            lo,
            mid,
            i,
            j
        )

        right = self._query(
            2 * tree_index + 2,
            mid + 1,
            hi,
            i,
            j
        )

        return self.merge(left, right)

    def merge(self, left, right):
        node = Node(self.k)

        node.prod = (left.prod * right.prod) % self.k

        # Elements coming from the left
        for i in range(self.k):
            node.remain[i] = left.remain[i]

        # Elements coming from the right
        for i in range(self.k):
            new_remainder = (i * left.prod) % self.k
            node.remain[new_remainder] += right.remain[i]

        return node


class Solution:
    def resultArray(self, nums, k, queries):

        # nums[i] %= k
        for i in range(len(nums)):
            nums[i] %= k

        # query[1] %= k
        for query in queries:
            query[1] %= k

        n = len(nums)

        ans = []

        tree = SegmentTree(nums, k)

        for query in queries:
            index = query[0]
            value = query[1]
            start = query[2]
            x = query[3]

            tree.update(index, value)

            result = tree.query(start, n - 1)

            ans.append(result.remain[x])

        return ans
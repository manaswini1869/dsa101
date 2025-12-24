class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        total_apples = sum(apple)
        m = len(capacity)
        capacity.sort(reverse=True)
        boxes = 0
        curr = 0
        for i in range(m):
            boxes += 1
            total_apples -= capacity[i]
            if total_apples <= 0:
                return boxes








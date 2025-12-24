class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        heap = []
        for no_box, no_unit in boxTypes:
            heapq.heappush(heap, (-no_unit, no_box))

        curr = 0
        curr_size = 0

        while curr_size < truckSize and heap:
            neg_units, boxes = heapq.heappop(heap)
            units = -neg_units

            take = min(boxes, truckSize - curr_size)
            curr += (take*units)
            curr_size += take
            # if curr_size + -boxes < truckSize:
            #     curr += (units*boxes)
            #     curr_size += -boxes
            # else:
            #     req = truckSize - curr_size
            #     curr += (req*-boxes)
            # if curr_size == truckSize:
            #     break

        return curr






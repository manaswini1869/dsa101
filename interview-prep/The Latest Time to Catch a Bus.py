from collections import defaultdict
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        taken = set(passengers)
        i = 0
        for bus in buses:
            count = 0
            while i < len(passengers) and passengers[i] <= bus and count < capacity:
                i += 1
                count += 1
        if count < capacity:
            candidate = buses[-1]
        else:
            candidate = passengers[i-1] - 1
        while candidate in taken:
            candidate -= 1
        return candidate
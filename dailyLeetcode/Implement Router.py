class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_queue = deque()
        self.unique_packets = set()
        self.dest_timestamps = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.unique_packets:
            return False
        if len(self.packet_queue) == self.memory_limit:
            oldest_packet = self.packet_queue.popleft()
            self.unique_packets.remove(oldest_packet)
            old_dest = oldest_packet[1]
            self.dest_timestamps[old_dest].popleft()
        self.unique_packets.add(packet)
        self.packet_queue.append(packet)
        self.dest_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_queue:
            return []

        source, destination, timestamp = self.packet_queue.popleft()
        self.unique_packets.remove((source, destination, timestamp))
        self.dest_timestamps[destination].popleft()
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_timestamps:
            return 0

        timestamps = self.dest_timestamps[destination]
        left_idx = bisect_left(timestamps, startTime)
        right_idx = bisect_right(timestamps, endTime)
        return right_idx - left_idx
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
from collections import deque, defaultdict
import bisect
class Router:
    router= deque();
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit;
        self.queue = deque();
        self.packetSet = set();
        self.destMap = defaultdict(list)
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp);
        if key in self.packetSet:
            return False;
        if len(self.queue) ==self.memoryLimit:
            old_source, old_destination, old_timestamp = self.queue.popleft();
            self.packetSet.remove((old_source, old_destination, old_timestamp))
            idx = bisect.bisect_left(self.destMap[old_destination], old_timestamp);
            if 0<=idx< len(self.destMap[old_destination]) and self.destMap[old_destination][idx] == old_timestamp:
                self.destMap[old_destination].pop(idx);
            if not self.destMap[old_destination]:
                del self.destMap[old_destination];
        self.queue.append((source, destination, timestamp));
        self.packetSet.add(key);
        self.destMap[destination].append(timestamp);
        return True;
            
    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return [];
        old_source, old_destination, old_timestamp = self.queue.popleft();
        self.packetSet.remove((old_source, old_destination, old_timestamp))
        idx = bisect.bisect_left(self.destMap[old_destination], old_timestamp);
        if 0<=idx< len(self.destMap[old_destination]) and self.destMap[old_destination][idx] == old_timestamp:
            self.destMap[old_destination].pop(idx);
        if not self.destMap[old_destination]:
            del self.destMap[old_destination];
        return[old_source, old_destination, old_timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0;
        timestamps = self.destMap[destination];
        left = bisect.bisect_left(timestamps, startTime);
        right = bisect.bisect_right(timestamps, endTime);
        return right - left;


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
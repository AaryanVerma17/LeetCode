from typing import List
import heapq
from bisect import bisect_left
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        request_count = [0] * k
        available = list(range(k))
        busy = []
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                idx = bisect_left(available, server_id)
                available.insert(idx, server_id)
            if not available:
                continue
            target = i % k
            idx = bisect_left(available, target)
            if idx == len(available):
                idx = 0
            server_id = available.pop(idx)
            request_count[server_id] += 1
            heapq.heappush(busy, (start + duration, server_id))
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]
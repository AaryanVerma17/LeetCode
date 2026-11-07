import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        idle = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(idle)
        busy = []
        result = []
        curr_time = 0
        for task_idx, task_duration in enumerate(tasks):
            curr_time = max(curr_time, task_idx)
            if not idle:
                curr_time = busy[0][0]
            while busy and busy[0][0] <= curr_time:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(idle, (weight, idx))
            weight, idx = heapq.heappop(idle)
            result.append(idx)
            heapq.heappush(busy, (curr_time + task_duration, weight, idx))
        return result
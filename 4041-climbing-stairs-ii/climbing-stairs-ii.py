from typing import List
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n == 0:
            return 0
        dp = [0, float('inf'), float('inf'), float('inf')]
        for i in range(1, n + 1):
            step_cost = costs[i - 1]
            min_cost = float('inf')
            for jump in range(1, 4):
                if i - jump >= 0:
                    prev_cost = dp[(i - jump) % 4]
                    total_cost = prev_cost + step_cost + (jump ** 2)
                    if total_cost < min_cost:
                        min_cost = total_cost
            dp[i % 4] = min_cost
        return dp[n % 4]
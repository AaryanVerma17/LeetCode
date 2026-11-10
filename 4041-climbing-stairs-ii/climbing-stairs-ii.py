from typing import List
import math
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            step_cost = costs[i - 1]
            for j in range(max(0, i - 3), i):
                jump_length = i - j
                transition_cost = dp[j] + step_cost + (jump_length ** 2)
                if transition_cost < dp[i]:
                    dp[i] = transition_cost     
        return dp[n]
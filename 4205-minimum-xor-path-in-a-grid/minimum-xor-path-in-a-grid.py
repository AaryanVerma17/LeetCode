class Solution:

  def minCost(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    MAX_XOR = 1024

    # dp[i][j][x] = True if XOR sum x is reachable at cell (i, j)
    dp = [[set() for _ in range(n)] for _ in range(m)]
    dp[0][0].add(grid[0][0])

    for i in range(m):
      for j in range(n):
        current_set = dp[i][j]
        if i + 1 < m:
          next_val = grid[i + 1][j]
          for xor_val in current_set:
            dp[i + 1][j].add(xor_val ^ next_val)
        if j + 1 < n:
          next_val = grid[i][j + 1]
          for xor_val in current_set:
            dp[i][j + 1].add(xor_val ^ next_val)

    return min(dp[m - 1][n - 1])

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            total_sum = grid[r][c]
            grid[r][c] = 0
            total_sum += dfs(r + 1, c)
            total_sum += dfs(r - 1, c)
            total_sum += dfs(r, c + 1)
            total_sum += dfs(r, c - 1)
            return total_sum
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        count += 1                    
        return count
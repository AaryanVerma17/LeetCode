class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_counts = [0] * ROWS
        col_counts = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        communicating_servers = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (row_counts[r] > 1 or col_counts[c] > 1):
                    communicating_servers += 1         
        return communicating_servers
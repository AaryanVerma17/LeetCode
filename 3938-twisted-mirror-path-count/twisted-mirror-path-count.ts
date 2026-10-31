function uniquePaths(grid: number[][]): number {
    const MOD = 1e9 + 7;
    const m = grid.length;
    const n = grid[0].length;
    let dp: number[][] = Array.from({ length: n + 1 }, () => [0, 0]);
    dp[1] = [1, 1];
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 1) {
                const prevDown = dp[c + 1][0];
                const prevRight = dp[c][1];
                dp[c + 1] = [prevRight, prevDown];
            } else {
                const total = (dp[c + 1][0] + dp[c][1]) % MOD;
                dp[c + 1] = [total, total];
            }
        }
    }
    return dp[n][0];
}
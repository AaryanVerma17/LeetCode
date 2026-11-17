class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_edits = INF
                for d in divisors[length]:
                    edits = 0
                    for rem in range(d):
                        left = i + rem
                        right = j - d + 1 + rem
                        while left < right:
                            if s[left] != s[right]:
                                edits += 1
                            left += d
                            right -= d
                    if edits < min_edits:
                        min_edits = edits
                cost[i][j] = min_edits
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for m in range(2 * (p - 1), i - 1):
                    if dp[m][p - 1] != INF:
                        dp[i][p] = min(dp[i][p], dp[m][p - 1] + cost[m][i - 1])                 
        return dp[n][k]
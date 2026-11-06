class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        q = sorted(enumerate(queries), key=lambda k: k[1])
        g = sorted(logs, key=lambda k: k[1])
        a = [0] * len(queries)
        m = {}
        c = 0
        l = 0
        r = 0
        for i, t in q:
            s = t - x
            e = t
            while r < len(g) and g[r][1] <= e:
                v = g[r][0]
                if m.get(v, 0) == 0:
                    c += 1
                m[v] = m.get(v, 0) + 1
                r += 1
            while l < len(g) and g[l][1] < s:
                v = g[l][0]
                m[v] -= 1
                if m[v] == 0:
                    c -= 1
                l += 1
            a[i] = n - c
        return a
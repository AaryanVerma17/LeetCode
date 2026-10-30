class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)

    def add(self, idx, val):
        idx += 1
        while idx <= self.size + 1:
            self.tree[idx] ^= val
            idx += idx & (-idx)

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & (-idx)
        return res

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = 16
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, 0, False)]
        path_masks = [0] * n
        initial_chars = [ord(c) - ord('a') for c in s]
        def dfs_precompute():
            nonlocal timer
            visited = [False] * n
            q = [(0, 0, 0)]
            order = []
            stack_tour = [0]
            visited_tour = [False] * n
            visited_tour[0] = True
            st = [(0, -1, 0)]
            tin_track = [0] * n
            tout_track = [0] * n
            t = 0
            adj_idx = [0] * n
            parent = [-1] * n
            path_masks[0] = 1 << initial_chars[0]
            
            curr = 0
            tin[0] = t
            t += 1
            
            while True:
                if adj_idx[curr] < len(adj[curr]):
                    nxt = adj[curr][adj_idx[curr]]
                    adj_idx[curr] += 1
                    if nxt != parent[curr]:
                        parent[nxt] = curr
                        depth[nxt] = depth[curr] + 1
                        up[nxt][0] = curr
                        for i in range(1, LOG):
                            up[nxt][i] = up[up[nxt][i-1]][i-1]
                        path_masks[nxt] = path_masks[curr] ^ (1 << initial_chars[nxt])
                        curr = nxt
                        tin[curr] = t
                        t += 1
                else:
                    tout[curr] = t
                    t += 1
                    if curr == 0:
                        break
                    curr = parent[curr]

        dfs_precompute()
        bit = FenwickTree(2 * n + 5)
        curr_chars = list(initial_chars)
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c_idx = ord(parts[2]) - ord('a')
                delta = (1 << curr_chars[u]) ^ (1 << c_idx)
                curr_chars[u] = c_idx
                bit.add(tin[u], delta)
                bit.add(tout[u] + 1, delta)
                
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                mask_u = path_masks[u] ^ bit.query(tin[u])
                mask_v = path_masks[v] ^ bit.query(tin[v])
                lca_char_mask = 1 << curr_chars[lca]
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans

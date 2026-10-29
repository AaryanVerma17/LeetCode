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
        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # 2. Flatten the tree using Euler Tour & Binary Lifting setup
        LOG = 16
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        # Iterative DFS to avoid deep recursion limits
        stack = [(0, 0, False)]  # (node, parent, processed)
        path_masks = [0] * n     # Initial root-to-node XOR masks
        initial_chars = [ord(c) - ord('a') for c in s]
        
        # Precompute initial masks during a standard traversal setup
        def dfs_precompute():
            nonlocal timer
            visited = [False] * n
            q = [(0, 0, 0)]  # node, p, dep
            order = []
            
            # Simple BFS/DFS to build topology
            stack_tour = [0]
            visited_tour = [False] * n
            visited_tour[0] = True
            
            # Build proper Euler tour bounds and parent pointers
            # Let's do a strict iterative DFS for Eulerian properties
            st = [(0, -1, 0)]
            tin_track = [0] * n
            tout_track = [0] * n
            t = 0
            
            # Reconstruct an explicit recursion stack
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
        
        # 3. Initialize Fenwick Tree with initial path states
        # Range update: point update at tin[u] and tin[u] is not enough for path prefix.
        # Instead of path prefixes directly inside BIT, we use BIT to store the changes (deltas).
        # Changing node u affects the subtree of u, which maps to range [tin[u], tout[u]].
        bit = FenwickTree(2 * n + 5)
        
        # Track current state of characters
        curr_chars = list(initial_chars)
        
        # 4. LCA helper function using binary lifting
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
                
                # XOR out the old char bit mask and XOR in the new char bit mask
                delta = (1 << curr_chars[u]) ^ (1 << c_idx)
                curr_chars[u] = c_idx
                
                # Apply range update to the subtree range [tin[u], tout[u]]
                bit.add(tin[u], delta)
                bit.add(tout[u] + 1, delta)
                
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                # Compute current root-to-node masks from initial + BIT adjustments
                mask_u = path_masks[u] ^ bit.query(tin[u])
                mask_v = path_masks[v] ^ bit.query(tin[v])
                
                # Character mask at the LCA node itself
                lca_char_mask = 1 << curr_chars[lca]
                
                # Combine values to get path parity mask
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                
                # Check if at most one bit is set
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans

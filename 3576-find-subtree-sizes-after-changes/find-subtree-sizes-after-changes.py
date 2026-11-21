class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)   
        sizes = [1] * n
        last_seen = [-1] * 26
        def dfs(u: int) -> None:
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]
            target_parent = prev_ancestor if prev_ancestor != -1 else parent[u]
            last_seen[char_idx] = u
            for v in adj[u]:
                dfs(v)
            last_seen[char_idx] = prev_ancestor
            if target_parent != -1:
                sizes[target_parent] += sizes[u]        
        dfs(0)
        return sizes
import java.util.*;

class Solution {
    public int shortestPath(int n, int[][] edges, String labels, int k) {
        // Step 1: Build the adjacency list for the directed graph
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(new int[]{edge[1], edge[2]}); // {destination, weight}
        }

        // Step 2: Initialize the 2D distance tracking array
        // dist[u][c] stores the minimum cost to reach node 'u' with 'c' consecutive identical characters ending at 'u'
        int[][] dist = new int[n][k + 1];
        for (int[] row : dist) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        
        // Min-Priority Queue ordered by path weight/cost: {cost, current_node, consecutive_count}
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        
        // Base case: Start at node 0 with a cost of 0 and a character sequence length of 1
        dist[0][1] = 0;
        pq.offer(new int[]{0, 0, 1});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int cost = curr[0];
            int u = curr[1];
            int count = curr[2];

            // If we find a path to the destination node n-1, it is guaranteed optimal by Dijkstra's properties
            if (u == n - 1) {
                return cost;
            }

            // Skip outdated states if a cheaper path to this state was already processed
            if (cost > dist[u][count]) {
                continue;
            }

            // Traverse all outgoing paths from node u
            for (int[] neighbor : graph[u]) {
                int v = neighbor[0];
                int weight = neighbor[1];

                // Calculate consecutive identical character count for the next node
                int nextCount = (labels.charAt(u) == labels.charAt(v)) ? count + 1 : 1;

                // If the constraint is respected and a shorter path to this state is found, relax the edge
                if (nextCount <= k && cost + weight < dist[v][nextCount]) {
                    dist[v][nextCount] = cost + weight;
                    pq.offer(new int[]{cost + weight, v, nextCount});
                }
            }
        }

        // Return -1 if node n-1 is unreachable within the given constraints
        return -1;
    }
}

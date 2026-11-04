import java.util.*;
class Solution {
    private static final long INF = Long.MAX_VALUE / 2;
    private static class BalancedWindowMap {
        public TreeMap<Integer, Integer> map = new TreeMap<>();
        public int size = 0;
        public long sum = 0;
        public void add(int val) {
            map.merge(val, 1, Integer::sum);
            sum += val;
            size++;
        }
        public void remove(int val) {
            if (map.containsKey(val)) {
                map.merge(val, -1, Integer::sum);
                if (map.get(val) == 0) {
                    map.remove(val);
                }
                sum -= val;
                size--;
            }
        }
    }
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;
        List<Long> minOps = getMinOps(nums, x);
        Long[][] mem = new Long[n + 1][k + 1];
        return solveDP(nums, x, 0, k, minOps, mem);
    }
    private long solveDP(int[] nums, int x, int i, int k, List<Long> minOps, Long[][] mem) {
        if (k == 0) return 0;
        if (i >= nums.length) return INF;
        if (mem[i][k] != null) return mem[i][k];
        long skip = solveDP(nums, x, i + 1, k, minOps, mem);
        long pick = INF;
        if (i + x <= nums.length) {
            pick = minOps.get(i) + solveDP(nums, x, i + x, k - 1, minOps, mem);
        }
        return mem[i][k] = Math.min(skip, pick);
    }
    private List<Long> getMinOps(int[] nums, int x) {
        int n = nums.length;
        List<Long> minOps = new ArrayList<>(Collections.nCopies(n, 0L));
        BalancedWindowMap lower = new BalancedWindowMap();
        BalancedWindowMap upper = new BalancedWindowMap();
        for (int i = 0; i < n; ++i) {
            if (lower.size == 0 || nums[i] <= lower.map.lastKey()) {
                lower.add(nums[i]);
            } else {
                upper.add(nums[i]);
            }
            if (i >= x) {
                int outNum = nums[i - x];
                if (lower.map.containsKey(outNum)) {
                    lower.remove(outNum);
                } else {
                    upper.remove(outNum);
                }
            }
            if (lower.size < upper.size) {
                int val = upper.map.firstKey();
                upper.remove(val);
                lower.add(val);
            } else if (lower.size - upper.size > 1) {
                int val = lower.map.lastKey();
                lower.remove(val);
                upper.add(val);
            }
            if (i >= x - 1) {
                int median = lower.map.lastKey();
                long cost = ((long) median * lower.size - lower.sum) + (upper.sum - (long) median * upper.size);
                minOps.set(i - x + 1, cost);
            }
        }
        return minOps;
    }
}
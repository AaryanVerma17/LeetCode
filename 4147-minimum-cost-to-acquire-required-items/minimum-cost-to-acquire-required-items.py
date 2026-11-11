class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        only_individual = (need1 * cost1) + (need2 * cost2)
        only_bundles = costBoth * max(need1, need2)
        shared = min(need1, need2)
        mixed_strategy = (costBoth * shared) + ((need1 - shared) * cost1) + ((need2 - shared) * cost2)
        return min(only_individual, only_bundles, mixed_strategy)
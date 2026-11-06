class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        shift = 2001
        limit = 4005
        k = [0] * limit
        for y in arr2:
            k[y + shift] = 1
        p = [0] * limit
        for i in range(1, limit):
            p[i] = p[i - 1] + k[i]
        c = 0
        for x in arr1:
            val = x + shift
            left = max(0, val - d)
            right = min(limit - 1, val + d)
            if (p[right] - (p[left - 1] if left > 0 else 0)) == 0:
                c += 1
        return c

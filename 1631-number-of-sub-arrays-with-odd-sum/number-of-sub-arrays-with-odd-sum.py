class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        m = 10**9 + 7
        ans = 0
        s = 0
        e = 1
        o = 0
        for x in arr:
            s += x
            if s % 2 != 0:
                ans = (ans + e) % m
                o += 1
            else:
                ans = (ans + o) % m
                e += 1
        return ans
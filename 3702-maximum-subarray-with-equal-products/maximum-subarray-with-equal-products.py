import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2
        i = 0
        take = 2
        while i + take <= n:
            sub = nums[i : i + take]
            if math.prod(sub) == math.gcd(*sub) * math.lcm(*sub):
                ans = max(ans, take)
                take += 1
            else:
                i += 1
                take = max(2, take - 1)
        return ans

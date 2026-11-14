class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)       
        for window_size in range(l, r + 1):
            curr_sum = sum(nums[:window_size])
            if curr_sum > 0:
                ans = min(ans, curr_sum)        
            for i in range(window_size, n):
                curr_sum += nums[i] - nums[i - window_size]
                if curr_sum > 0:
                    ans = min(ans, curr_sum)  
        return ans if ans != float('inf') else -1
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digits = [int(d) for d in str(nums[i])]
            if sum(digits) == i:
                return i
        return -1

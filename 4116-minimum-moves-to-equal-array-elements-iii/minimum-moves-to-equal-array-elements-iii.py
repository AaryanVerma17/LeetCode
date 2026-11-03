class Solution:
    def minMoves(self, nums: List[int]) -> int:
        diff = []
        max_element = max(nums)
        for i in range(len(nums)):
            new_element = max_element - nums[i]
            diff.append(new_element)
        return sum(diff)
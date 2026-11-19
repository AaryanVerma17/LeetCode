class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],  # Change two smallest
            nums[-3] - nums[0],  # Change two largest
            nums[-2] - nums[1]   # Change one smallest and one largest
        )
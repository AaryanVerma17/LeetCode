class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

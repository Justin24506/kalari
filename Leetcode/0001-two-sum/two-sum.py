# https://leetcode.com/problems/two-sum/submissions/2111531306
# Runtime 1734 ms
# Memory 19.83 MB


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return []

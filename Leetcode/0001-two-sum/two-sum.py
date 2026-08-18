# https://leetcode.com/problems/two-sum/submissions/2111502116
# Runtime 2083 ms
# Memory 19.72 MB


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    output = [i, j]
        return output

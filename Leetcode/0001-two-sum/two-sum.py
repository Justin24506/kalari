# https://leetcode.com/problems/two-sum/submissions/2111635943
# Runtime 0 ms
# Memory 20.54 MB


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}
        for index, num in enumerate(nums):
            if target - num not in dict_nums:
                dict_nums[num] = index
            else:
                return [index, dict_nums[target - num]]
        return []

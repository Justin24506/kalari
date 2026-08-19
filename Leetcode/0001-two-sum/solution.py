# https://leetcode.com/problems/two-sum/submissions/2111657912
# Runtime 0 ms
# Memory 20.48 MB


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}
        for index, num in enumerate(nums):
            if target - num not in dict_nums:
                dict_nums[num] = index
            else:
                return [dict_nums[target - num], index]
        return []

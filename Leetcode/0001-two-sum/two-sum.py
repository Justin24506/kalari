# https://leetcode.com/problems/two-sum/submissions/2111626253
# Runtime 0 ms
# Memory 20.34 MB


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if rem not in dict_nums:
                dict_nums[nums[i]] = i
            else:
                return [i, dict_nums[rem]]
        return []

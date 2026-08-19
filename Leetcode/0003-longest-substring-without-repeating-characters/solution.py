# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2112630574
# Runtime: 152 ms
# Memory: 19.91 MB


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: dict[str, int] = {}
        left = 0
        max_len = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = i
            max_len = max(max_len, i - left + 1)

        return max_len

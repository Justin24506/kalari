# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2112592442
# Runtime: 203 ms
# Memory: 19.92 MB


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen: set[str] = set()
        left = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            max_len = max(max_len, i - left + 1)
        return max_len

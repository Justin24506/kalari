# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2112557815
# Runtime: 208 ms
# Memory: 20.01 MB


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        log = ""
        max_length = 0
        for i in range(len(s)):
            if s[i] in log:
                log += s[i]
                dupi = log.index(s[i])
                log = log[dupi + 1 :]

            else:
                log += s[i]

            max_length = max(len(log), max_length)

        return max_length

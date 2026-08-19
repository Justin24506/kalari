# https://leetcode.com/problems/palindrome-number/submissions/2112809647
# Runtime: 5 ms
# Memory: 19.21 MB


class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        workx = x

        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        while rev < workx:
            rev = rev * 10 + (workx % 10)
            workx = workx // 10

        return (workx == rev) or (workx == rev // 10)

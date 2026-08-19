# https://leetcode.com/problems/palindrome-number/submissions/2112792503
# Runtime: 8 ms
# Memory: 19.29 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        workx = x
        if x < 0:
            return False
        elif x > 0 and x % 10 == 0:
            return False
        while workx:
            rev = rev * 10 + (workx % 10)
            workx = workx // 10

        return x == rev

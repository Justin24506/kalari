# https://leetcode.com/problems/palindrome-number/submissions/2112775378
# Runtime: 38 ms
# Memory: 19.27 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev= 0
        ex = -1
        x2 = x
        x3 = x
        if x < 0:
            x = abs(x)
            x2 = x
        while x2:
            ex += 1
            x2 = x2//10
        while x:
            rev += (x % 10)  * (10 ** ex)
            x = x // 10
            ex -= 1

        return (x3 == rev)

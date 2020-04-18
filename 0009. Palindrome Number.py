
"""
Determine whether an integer is a palindrome. Do this without extra space.
https://leetcode.com/problems/palindrome-number/#/description
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        p = 0
        q = x
        while q >= 10:
            p += q%10
            p *= 10
            q /= 10
        p = p + q
        return p == x


if __name__ == '__main__':
    print Solution().isPalindrome(2111)
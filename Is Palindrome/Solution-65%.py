class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
        

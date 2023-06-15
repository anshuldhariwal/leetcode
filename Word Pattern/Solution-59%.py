class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            if pattern.find(pattern[i]) != words.index(words[i]):
                return False

        return True

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}

        result = 0
        prev = 0
        for i in s:
            value = dict[i]
            if prev == 0:
                prev = value
                result += value
            elif prev < value:
                result -= prev*2
                result += value
                prev = value
            else:
                result += value
                prev = value
            
        return result

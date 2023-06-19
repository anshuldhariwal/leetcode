class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        value = 0
        for i in gain:
            value += i
            highest = max(value, highest)

        return highest

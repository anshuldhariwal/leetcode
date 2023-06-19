class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return n

        value = [-1] * n
        value[0] = 1
        value[1] = 2

        for i in range(2, n):
            value[i] = value[i-1] + value[i-2]

        return value[n-1]

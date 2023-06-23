class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height) - 1
        area = 0

        if len(height) == 2:
            return min(height[0],height[1])

        while i < j:
            area = max(min(height[i],height[j]) * (j-i), area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area

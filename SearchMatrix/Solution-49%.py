class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for i in matrix:
            if target <= i[-1]:
                for j in i:
                    if j == target:
                        return True
        
        return False

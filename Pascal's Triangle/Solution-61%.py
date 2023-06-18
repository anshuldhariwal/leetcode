class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        result = [[1],[1,1]]
        for i in range(2,numRows):
            prev = result[i-1]
            add = [1] * (i+1)
            for j in range(len(prev)-1):
                add[j+1] = prev[j] + prev[j+1]
            result.append(add)

        return result

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        prev = 1
        result.append(prev)

        for i in range(1, rowIndex + 1):
            curr = (prev * (rowIndex - i + 1)) // i
            result.append(curr)
            prev = curr

        return result

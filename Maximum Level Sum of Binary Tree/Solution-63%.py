# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sumValue = {}
        def sumLevels(root, depth):
            if root:
                try:
                    sumValue[depth] += root.val
                except:
                    sumValue[depth] = root.val

                sumLevels(root.left, depth+1)
                sumLevels(root.right, depth+1)

        sumLevels(root, 1)

        maxValue = sumValue[1]
        k = 1
        for key in sumValue:
            if sumValue[key] > maxValue:
                k = key
                maxValue = sumValue[key]
        return k

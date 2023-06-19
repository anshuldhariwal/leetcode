# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

        # def preorder(root):
        #     return [root.val] + preorder(root.left) + preorder(root.right) if root else []

        # def postorder(root):
        #     return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

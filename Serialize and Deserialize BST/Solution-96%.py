# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []

        if not root:
            return ""

        def iterator(node):
            if not node:
                result.append("end")
                return
            
            result.append(str(node.val))
            iterator(node.left)
            iterator(node.right)
        
        iterator(root)
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        self.i = 0
        data = data.split(",")

        def iterator(node):
            node.val = data[self.i]

            self.i += 1
            if data[self.i] != "end":
                node.left = iterator(TreeNode())
            
            self.i += 1
            if data[self.i] != "end":
                node.right = iterator(TreeNode())

            return node

        return iterator(TreeNode())
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

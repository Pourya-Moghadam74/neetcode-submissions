# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def diameter(node):
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return 1
            
            left = diameter(node.left)
            right = diameter(node.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        diameter(root)
        return self.res
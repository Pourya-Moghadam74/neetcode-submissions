# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):

            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                return 1
            
            return 1 + max(depth(root.left), depth(root.right))
        

        return depth(root)

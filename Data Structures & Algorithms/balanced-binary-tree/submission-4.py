# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbal = True

        def dfs(node):
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) <= 1:
                return 1 + max(left, right)
            
            else:
                return float('inf')
        
        return True if dfs(root) != float('inf') else False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, p, q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.helper(p.left, q.left) and self.helper(p.right, q.right)
        
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        
        def dfs(node):
            if node is None:
                return False
                
            if self.helper(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)


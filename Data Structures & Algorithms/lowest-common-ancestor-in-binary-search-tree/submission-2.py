# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None

        def dfs(node):
            if node is None:
                return
            
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                self.ans = node
                return
            
            if p.val > node.val:
                dfs(node.right)
            
            else:
                dfs(node.left)
            
        dfs(root)

        return self.ans
            
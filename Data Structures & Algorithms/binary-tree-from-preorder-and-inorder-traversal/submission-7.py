# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for idx, val in enumerate(inorder):
            indices[val] = idx
        
        self.root_idx = 0
        def dfs(l, r):
            if l > r:
                return
            
            root_val = preorder[self.root_idx]
            self.root_idx += 1
            root = TreeNode(root_val)
            m = indices[root_val]
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)
            return root
        


        return dfs(0, len(preorder) - 1)
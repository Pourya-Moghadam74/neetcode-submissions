# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.rootIdx = 0

        def dfs(l, r):
            if l > r:
                return
            
            rootVal = preorder[self.rootIdx]
            self.rootIdx += 1
            root = TreeNode(rootVal)
            m = indices[rootVal]
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)


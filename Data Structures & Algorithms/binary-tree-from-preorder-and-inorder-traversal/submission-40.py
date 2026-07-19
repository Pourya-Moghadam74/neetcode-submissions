# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return
            rootVal = preorder[0]
            root = TreeNode(rootVal)
            m = inorder.index(rootVal)
            root.left = dfs(preorder[1 : m + 1], inorder[ : m])
            root.right = dfs(preorder[m + 1 : ], inorder[m + 1: ])
            return root
        
        return dfs(preorder, inorder)


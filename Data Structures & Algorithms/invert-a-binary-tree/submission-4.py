# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque


        def bfs(root):
            q = deque([root])
            if root is None:
                return None

            while q:
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            return root

        # return bfs(root)


        def dfs(root):

            if root is None:
                return None
            
            root.left, root.right = root.right, root.left

            dfs(root.left)
            dfs(root.right)
            
            return root
            
        return dfs(root)
        














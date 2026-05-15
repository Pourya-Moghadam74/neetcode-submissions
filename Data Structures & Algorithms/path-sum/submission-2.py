# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, currSum):

            if root is None:
                return False
            
            currSum += root.val

            if root.right is None and root.left is None:
                if currSum == targetSum:
                    return True
                else:
                    return False
            
            return dfs(root.left, currSum) or dfs(root.right, currSum)
        
        return dfs(root, 0)
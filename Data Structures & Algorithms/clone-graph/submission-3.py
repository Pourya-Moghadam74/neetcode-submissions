"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToCopy = {}
        if node is None:
            return None
            
        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            
            nodeCopy = Node(node.val)
            oldToCopy[node] = nodeCopy

            for n in node.neighbors:
                nCopy = dfs(n)
                nodeCopy.neighbors.append(nCopy)
            
            return nodeCopy
        
        dfs(node)

        return oldToCopy[node]
            
        

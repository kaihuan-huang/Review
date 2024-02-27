# Depth-First-Search(DFS): get to the bottom of the tree 
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, m):
            nonlocal res
            if not root:
                return
            
            if root.val >= m:
                res += 1

            n = max(m, root.val)
            dfs(root.left, n)
            dfs(root.right, n)
        
        dfs(root, float('-inf'))
        return res
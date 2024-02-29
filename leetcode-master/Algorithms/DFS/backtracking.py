'''Q: Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes
Backtracking: go throught every possibility way to the end O(n)
'''
'''1. return Ture if there have the path, False...'''
 def canReachLeaf(root):
     if not root or root.val == 0:
         return False
     
     if not root.left and not root.right:
         return True
     if canReachLeaf(root.left):
         return True
     if canReachLeaf(root.right):
         return True
     return False
 
 '''2. Return the value of that path'''
 def leafPath(root, path):
     if not root or root.val == 0:
         return False
     path.append(root.val)
     
     if not root.left and not root.right:
         return True
     if leafPath(root.left, path):
         return True
     if leafPath(root.right, path):
         return True
     path.pop()
     return False
 
 
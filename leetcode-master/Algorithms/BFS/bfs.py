#BST-Remove
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.validator
            root.right = remove(root.right, minNode.val)
    return root

#BST - Traversal
# 1. In Order Travesal (print form smallest to largest)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)  
# 2. reverse-order travesal (print the value from lagest to smallest)
def reverse(root):
    if not root:
        return
    reverse(root.right)
    print(root.val)
    reverse(root.left)
    
# 2. Pre Order Traversal
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.val)
    preorder(root.right)
# 3. Post Order Travesal
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
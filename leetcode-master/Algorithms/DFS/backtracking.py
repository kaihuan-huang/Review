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
 
 '''Subsets 
 Q: Given a list of distinct nums, return all possible distinct subsets
    include the empty list 
    *** diatinct == no duplicates
 '''
# Time: O(N*2^n) >> O(n) = Space Complexity
def subsestWithoutDuplicates(nums):
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    return subsets

def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    # decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()
    
    # decision NOT to include nums[i]
    helper(i + 1, nums, curSet, subsets)
    
'''If the subsets contain duplicates?
Q: Given a list of number that are not necessary distinct, return all distinct subsets
when we reach duplicate values skipping all of them
'''
# Time: O(N*2^n) >> O(n) = Space Complexity
def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curSet = [], []
    helper2(0, nums, curSet, subsets)
    return subsets
def helper2(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    #decision to include nums[i]
    curSet.append(nums[i])
    helper2(i + 1, nums, curSet, subsets)
    curSet.pop()
    
    # *** decision NOT to include nums[i]: when we reach duplicate values skipping all of them
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, curSet, subsets)
    
'''Combinations
Q: Given two nums n & k, return all possible combinaitons of size=k, choosing from values between 1 and n.
'''
# TC: O(k * C(n, k))
def combinations(n, k):
    combs = []
    helper3(1, [], combs, n, k)
    return combs

def helper3(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curCombs.copy())
        return
    if i > n:
        return
    
    for j in range(i, n + 1):
        curComb.append(j)
        helper3(j + 1, curComb, combs, n, k)
        curComb.pop()
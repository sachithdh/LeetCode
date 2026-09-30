# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,l_sub, r_sub):
        if (not l_sub and r_sub) or (l_sub and not r_sub):
            return False
        if (not l_sub and not r_sub):
            return True

        if l_sub.val != r_sub.val:
            return False
        
        return self.helper(l_sub.left, r_sub.right) and self.helper(l_sub.right, r_sub.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.helper(root.left, root.right)
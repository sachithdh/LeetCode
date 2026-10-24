# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        l = []
        
        l += self.postorderTraversal(root.left)
        l += self.postorderTraversal(root.right)
        l.append(root.val)

        return l
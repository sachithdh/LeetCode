# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepthHelper(self, root: TreeNode | None) -> int:
        if root is None:
            return -1

        lDepth = self.getDepthHelper(root.left)
        rDepth = self.getDepthHelper(root.right)

        return max(lDepth, rDepth) + 1

    def maxDepth(self, root: TreeNode | None) -> int:
        return self.getDepthHelper(root) + 1
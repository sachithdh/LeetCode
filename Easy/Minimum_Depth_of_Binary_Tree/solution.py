# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root):
        if root is None:
            return -1
        lDepth = self.getDepth(root.left) + 1
        rDepth = self.getDepth(root.right) + 1

        print(lDepth)
        print(rDepth)
        print()
        if lDepth == 0:
            return rDepth
        elif rDepth == 0:
            return lDepth
        else:
            return min(lDepth, rDepth)
    def minDepth(self, root: TreeNode | None) -> int:
        return self.getDepth(root) + 1
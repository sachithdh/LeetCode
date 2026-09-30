# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy
class Solution:
    def traversal(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        l = []
        if root.left:
            l += self.traversal(root.left)
        if root.right and not root.left:
            l.append("null")
        l.append(str(root.val))

        if root.right:
            l += self.traversal(root.right)
        if root.left and not root.right:
            l.append("null")
        
        return l

    def mirror(self, node: TreeNode | None) -> TreeNode | None:
        if not node:
            return

        left = node.left
        right = node.right

        node.left = self.mirror(right)
        node.right = self.mirror(left)

        return node


    def isSymmetric(self, root: TreeNode | None) -> bool:
        original = copy.deepcopy(root)
        mirror_root = self.mirror(root)
        return self.traversal(original) == self.traversal(mirror_root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
    def isSymmetric(self, root: TreeNode | None) -> bool:

        l = self.traversal(root)
        n = len(l)
        if n % 2 == 0:
            return False
        mid = int((n + 1) / 2)
        
        print(l)
        print(l[:mid - 1])
        print(l[-1:-mid:-1])

        return l[:mid - 1] == l[-1:-mid:-1]
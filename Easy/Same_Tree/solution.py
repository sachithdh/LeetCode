# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        
        l = []
        l.append(str(root.val))
        if root.left:
            l += self.preorderTraversal(root.left)
        
        if not root.left:
            l.append("null")

        if root.right:
            l += self.preorderTraversal(root.right)
        if not root.right:
            l.append("null")
        return l

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        l1 = self.preorderTraversal(p)
        l2 = self.preorderTraversal(q)

        print("l1: ", l1)
        print("l1: ", l2)

        return l1 == l2
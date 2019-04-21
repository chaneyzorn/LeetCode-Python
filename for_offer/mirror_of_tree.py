# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Mirror(self, root):
        if not root:
            return None
        left = self.Mirror(root.left)
        right = self.Mirror(root.right)
        root.left, root.right = right, left
        return root

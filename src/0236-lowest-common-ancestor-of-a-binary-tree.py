# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None

        def rescurse_tree(root):
            if not root:
                return 0

            mid, left, right = 0, 0, 0
            if root in (p, q):
                mid = 1
            left = rescurse_tree(root.left)
            right = rescurse_tree(root.right)

            if mid + left + right > 1:
                self.ans = root
            return mid or left or right

        rescurse_tree(root)
        return self.ans

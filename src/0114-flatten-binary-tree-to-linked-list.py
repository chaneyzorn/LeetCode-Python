# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                most_right = curr.left
                while most_right.right:
                    most_right = most_right.right
                most_right.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

    # def __init__(self):
    #     self.curr = None
    #
    # def flatten(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: None Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return
    #     self.flatten(root.right)
    #     self.flatten(root.left)
    #     root.right = self.curr
    #     root.left = None
    #     self.curr = root

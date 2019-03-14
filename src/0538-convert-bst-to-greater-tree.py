# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def get_right_min(node):
            succ = node.right
            while succ.left and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        cur = root

        while cur:
            if not cur.right:
                total += cur.val
                cur.val = total
                cur = cur.left
            else:
                succ = get_right_min(cur)
                if not succ.left:
                    succ.left = cur
                    cur = cur.right
                else:
                    succ.left = None
                    total += cur.val
                    cur.val = total
                    cur = cur.left
        return root


    # def __init__(self):
    #     self.total = 0
    #
    # def convertBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if not root:
    #         return root
    #
    #     self.convertBST(root.right)
    #     self.total += root.val
    #     root.val = self.total
    #     self.convertBST(root.left)
    #     return root

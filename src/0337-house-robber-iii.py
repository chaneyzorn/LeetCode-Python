# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rob_record = {}

        def rob_tree(root):
            if not root:
                return 0
            if root in rob_record:
                return rob_record[root]
            result = max(rob_child(root), root.val + rob_child(root.left) + rob_child(root.right))

            rob_record[root] = result
            return result

        def rob_child(node):
            if not node:
                return 0
            return rob_tree(node.left) + rob_tree(node.right)

        return rob_tree(root)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rob3(root):
            if not root:
                return 0, 0, 0
            l, ll, lr = rob3(root.left)
            r, rl, rr = rob3(root.right)
            return max(root.val + ll + lr + rl + rr, l + r), l, r

        return rob3(root)[0]

    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #
    #     def re_rob(root):
    #         res = [0, 0]
    #         if not root:
    #             return
    #
    #         left_rob = re_rob(root.left)
    #         right_rob = re_rob(root.right)
    #         res[0] = max(left_rob[0], left_rob[1]) + max(right_rob[0], right_rob[1])
    #         res[1] = root.val + left_rob[0] + right_rob[0]
    #         return res
    #
    #     res = re_rob(root)
    #     return max(res[0], res[1])

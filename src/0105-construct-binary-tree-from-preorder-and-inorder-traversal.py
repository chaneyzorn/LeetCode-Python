# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        N = len(inorder)
        pre_iter = iter(preorder)
        in_dict = {val: i for i, val in enumerate(inorder)}

        def recurse(start, end):
            if start > end:
                return None
            val = next(pre_iter)
            index = in_dict[val]
            root = TreeNode(val)
            root.left = recurse(start, index - 1)
            root.right = recurse(index + 1, end)
            return root

        return recurse(0, N - 1)

    # def buildTree(self, preorder, inorder):
    #     """
    #     :type preorder: List[int]
    #     :type inorder: List[int]
    #     :rtype: TreeNode
    #     """
    #     if not inorder:
    #         return None
    #     index = inorder.index(preorder[0])
    #     root = TreeNode(inorder[index])
    #     root.left = self.buildTree(preorder[1:], inorder[:index])
    #     root.right = self.buildTree(preorder[1:], inorder[index + 1:])
    #     return root

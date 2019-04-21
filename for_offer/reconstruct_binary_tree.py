class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        pre_iter = iter(pre)
        tin_dict = {v: i for i, v in enumerate(tin)}

        def recurse(left, right):
            if left > right:
                return None
            val = next(pre_iter)
            index = tin_dict[val]
            root = TreeNode(val)

            root.left = recurse(left, index - 1)
            root.right = recurse(index + 1, right)
            return root

        return recurse(0, len(tin) - 1)

    # def reConstructBinaryTree(self, pre, tin):
    #     if not tin:
    #         return None
    #     index = tin.index(pre.pop(0))
    #
    #     root = TreeNode(tin[index])
    #     root.left = self.reConstructBinaryTree(pre, tin[:index])
    #     root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
    #     return root

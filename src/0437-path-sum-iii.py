# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNodes
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, 0, {0: 1})

    def helper(self, root, target, curr_sum, cache):
        if not root:
            return 0
        curr_sum += root.val

        result = cache.get(curr_sum - target, 0)
        cache[curr_sum] = cache.get(curr_sum, 0) + 1
        result += self.helper(root.left, target, curr_sum, cache) + self.helper(root.right, target, curr_sum, cache)
        cache[curr_sum] -= 1
        return result


    # def pathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     # 自身参与的链式任务
    #     count = self.linkedSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    #     return count
    #
    # def linkedSum(self, root, sum):
    #     if not root:
    #         return 0
    #
    #     count = 0
    #     if root.val == sum:
    #         count += 1
    #     extra = sum - root.val
    #     count = count + self.linkedSum(root.left, extra) + self.linkedSum(root.right, extra)
    #     return count

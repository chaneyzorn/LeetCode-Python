class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not (pRoot1 and pRoot2):
            return False
        result = False
        if pRoot1.val == pRoot2.val:
            result = self.SameTree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def SameTree(self, t1, t2):
        if t2 is None:
            return True
        if t1 is None:
            return False

        if t1.val != t2.val:
            return False
        return self.SameTree(t1.left, t2.left) and self.SameTree(t1.right, t2.right)

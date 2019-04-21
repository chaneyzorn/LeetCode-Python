# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return listNode

        new_head = None
        curr = listNode
        while curr:
            next = curr.next
            curr.next = new_head
            new_head = curr
            curr = next

        result = []
        while new_head:
            result.append(new_head.val)
            new_head = new_head.next
        return result

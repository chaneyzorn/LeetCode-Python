# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        head = None
        while pHead:
            next = pHead.next
            pHead.next = head
            head = pHead
            pHead = next
        return head

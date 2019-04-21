# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        p1, p2 = head, head
        while k and p1:
            p1 = p1.next
            k -= 1
        if k > 0:
            return None

        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2

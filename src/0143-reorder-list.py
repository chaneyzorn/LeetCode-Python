"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not (head and head.next and head.next.next):
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        res_mid = None
        while mid:
            temp = mid.next
            mid.next = res_mid
            res_mid = mid
            mid = temp

        while head and res_mid:
            head_temp = head.next
            res_mid_temp = res_mid.next

            res_mid.next = head_temp
            head.next = res_mid

            head = head_temp
            res_mid = res_mid_temp

    # def reorderList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: void Do not return anything, modify head in-place instead.
    #     """
    #     if not (head and head.next and head.next.next):
    #         return head
    #
    #     curr = head
    #     while curr and curr.next:
    #         prev, tail = curr, curr.next
    #         while tail.next:
    #             prev = tail
    #             tail = tail.next
    #         prev.next = None
    #         tail.next = curr.next
    #         curr.next = tail
    #         curr = tail.next

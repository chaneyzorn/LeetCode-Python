"""
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        l_curr = l_list = ListNode(0)
        ge_curr = ge_list = ListNode(0)
        while head:
            next = head.next
            head.next = None

            if head.val < x:
                l_curr.next = head
                l_curr = l_curr.next
            else:
                ge_curr.next = head
                ge_curr = ge_curr.next

            head = next

        l_curr.next = ge_list.next
        return l_list.next

"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        prev = dummy = ListNode(0)
        one = dummy.next = head

        while one and one.next:
            another = one.next
            duplicate = None
            while another and one.val == another.val:
                duplicate = another
                another = another.next
            if duplicate:
                prev.next = another
            else:
                prev = prev.next
            one = another

        return dummy.next

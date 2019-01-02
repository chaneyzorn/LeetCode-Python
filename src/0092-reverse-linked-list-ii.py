"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        before = dummy = ListNode(0)
        before.next = head

        for i in range(m - 1):
            before = before.next

        res_head = None
        curr = res_tail = before.next
        while m != (n + 1):
            next = curr.next
            curr.next = res_head
            res_head = curr
            curr = next
            m += 1

        before.next = res_head
        res_tail.next = curr
        return dummy.next

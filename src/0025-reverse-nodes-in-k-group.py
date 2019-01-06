"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not (head and head.next and k > 1):
            return head

        processed = dummy = ListNode(0)
        remained = dummy.next = head

        while remained:
            count = 0
            start = remained
            while count < k and remained:
                remained = remained.next
                count += 1
            if count == k:
                curr, sub_head = start, remained
                while curr is not remained:
                    temp = curr.next
                    curr.next = sub_head
                    sub_head = curr
                    curr = temp
                processed.next = sub_head
                processed = start
        return dummy.next


"""
k = 3 for example:

step 0: a -> b -> c -> (next k-group)

step 1:      b -> c -> (next k-group)
                  a ---^

step 2:           c -> (next k-group)
             b -> a ---^

step 3:                (next k-group)
        c -> b -> a ---^

finish: c -> b -> a -> (next k-group)

"""

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:       a1 --> a2 ---.
                      c1 --> c2
B: b1 --> b2 --> b3 --`

begin to intersect at node c1.

Example 1:

A:       4 --> 1 ---.
                    8 --> 4 --> 5
B: 5 --> 0 --> 1 --`

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

A: 0 --> 9 --> 1 ---.
                    2 --> 4
B:            3 ---`

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:

A: 2 --> 6 --> 4

B:       1 --> 5

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4].
From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return None
        len_A = self._get_len(headA)
        len_B = self._get_len(headB)
        if len_A >= len_B:
            p1 = self._relocate_linked_list(headA, len_A - len_B)
            p2 = headB
        else:
            p1 = headA
            p2 = self._relocate_linked_list(headB, len_B - len_A)

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1 if p1 == p2 else None

    def _get_len(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def _relocate_linked_list(self, head, offset):
        while offset > 0:
            head = head.next
            offset -= 1
        return head


"""
A:     A --> A --> A --> A --> C --> D --> D
B:                 B --> B --> C --> D --> D
                               ^

A + B: A --> A --> A --> A --> C --> D --> D --> B --> B --> C --> D --> D
B + A: B --> B --> C --> D --> D --> A --> A --> A --> A --> C --> D --> D
                   ^           ^                             ^
"""


# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         if not (headA and headB):
#             return None
#
#         A_pointer = headA
#         B_pointer = headB
#
#         while A_pointer != B_pointer:
#             A_pointer = headB if A_pointer == None else A_pointer.next
#             B_pointer = headA if B_pointer == None else B_pointer.next
#
#         return A_pointer


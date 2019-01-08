"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        curr = dummy = ListNode(0)
        lists = [item for item in lists if item]
        lists.sort(key=lambda item: item.val)

        while lists:
            node = lists[0]
            curr.next = node
            curr = curr.next
            lists[0] = lists[0].next
            node = lists.pop(0)
            lists = self.relocate(lists, node)
        return dummy.next

    def relocate(self, lists, node):
        if not node:
            return lists
        low, high = 0, len(lists) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if lists[mid].val > node.val:
                high = mid - 1
            else:
                low = mid + 1
        lists.insert(low, node)
        return lists


class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge_two(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def merge_two(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

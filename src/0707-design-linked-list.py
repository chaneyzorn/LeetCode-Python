"""
Design your implementation of the linked list.
You can choose to use the singly linked list or the doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list,
you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        node = ListNode(0)  # dummy
        self.head = node
        self.tail = node
        self.len = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.len:
            return -1
        p = self.head.next
        while index > 0:
            index -= 1
            p = p.next
        return p.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if self.head is self.tail:
            self.tail = node
        self.len += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.len += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.len:
            return
        p = self.head
        while index > 0:
            index -= 1
            p = p.next

        node = ListNode(val)
        node.next = p.next
        p.next = node

        if p is self.tail:
            self.tail = node
        self.len += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.len:
            return
        p = self.head
        while index > 0:
            index -= 1
            p = p.next
        if p.next is self.tail:
            self.tail = p
        p.next = p.next.next
        self.len -= 1

    def __str__(self):
        p = self.head.next
        li = []
        while p:
            li.append(str(p.val))
            p = p.next
        return "-->".join(li)


if __name__ == '__main__':
    call_name = [
        "addAtHead", "get", "addAtTail", "addAtIndex", "addAtHead",
        "addAtIndex", "addAtTail", "addAtTail", "addAtIndex", "get", "addAtTail"
    ]
    args = [[0], [1], [2], [1, 4], [4], [1, 4], [5], [2], [2, 0], [2], [1]]

    linkedList = MyLinkedList()
    for fn, arg in zip(call_name, args):
        arg_str = ','.join([str(item) for item in arg])
        print(f"{fn}({arg_str})", getattr(linkedList, fn)(*arg), linkedList)

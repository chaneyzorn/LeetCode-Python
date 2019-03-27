class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain = capacity
        self.db = {}
        self.l_start = Node(None, None)
        self.l_end = Node(None, None)
        self.l_start.next = self.l_end
        self.l_end.prev = self.l_start

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.db.get(key)
        if node:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node.next = self.l_start.next
            node.next.prev = node
            node.prev = self.l_start
            self.l_start.next = node
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        invalid = False
        if key in self.db:
            node = self.db.get(key)
            node.val = value
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            node = Node(key, value)
            self.db[key] = node
            if self.remain <= 0:
                invalid = True
            else:
                self.remain -= 1

        node.next = self.l_start.next
        node.next.prev = node
        node.prev = self.l_start
        self.l_start.next = node

        if invalid:
            invalid_node = self.l_end.prev
            tail = invalid_node.prev
            tail.next = self.l_end
            self.l_end.prev = tail
            invalid_node.prev = None
            invalid_node.next = None
            self.db.pop(invalid_node.key)

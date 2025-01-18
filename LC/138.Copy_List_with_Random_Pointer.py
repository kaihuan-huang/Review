"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Create new noded and insert them right after original nodes
        c = head
        while c:
            new_node = Node(c.val)
            new_node.next = c.next
            c.next = new_node
            c = new_node.next

        # Assign random pointers for the new nodes
        c = head
        while c:
            if c.random:
                c.next.random = c.random.next
            c = c.next.next

        # Separate the new list from the old list
        c = head
        new_head = head.next
        while c:
            new_node = c.next
            c.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            c = c.next
        return new_head
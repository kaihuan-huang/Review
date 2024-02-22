class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
# setting the next pointer for ListNode2 and ListNode3
ListNode1.next = ListNode2
ListNode2.next = ListNode3
ListNode3.next = null

#Traversal: to traverse a linked list from beginning to end, using while loop:
cur = ListNode1
while cur:
    cur = cur.next

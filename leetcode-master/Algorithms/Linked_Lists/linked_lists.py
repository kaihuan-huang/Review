'''1. Singly Linked Lists'''

'''2. Doubly Linked Lists'''
tail.next = ListNode4
ListNode4.prev = tail
tail = tail.next

# Doubly Linked Lists: we can insert 

'''Queues: FIFO First In First Out'''

'''Fast and Slow Pointer
Q: Find the middle of a linked list
TC: O(n); SC: O(1)
'''
def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
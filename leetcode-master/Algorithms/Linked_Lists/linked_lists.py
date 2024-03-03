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

'''Fast and Slow Linked Lists for cycle detection
Q: Dertemine if a linked list has a cycle
TC: O(n) SC: O(1)
'''
def hasCycle(head):
    # initialize slow & fast pointer to head
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next # add slow pointer by 1
        fast = fast.next.next # add faster pointer by 2
        if slow == fast:
            return True # there has a cycle
    return Fasle # Out of the cycle, there not a cycle

'''Fast and Slow pointer:
Q: Determine is a linked list has a cycle and return the head, else return null.
TC: O(n) SC: O(1)
'''
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # keep looping throuth slow and fast pointer until equal to each other, break out from the loop = fast pointer might go out of bounds, which means we reach the end of linked list
        if slow == fast:
            break
        
    if not fast or not fast.next:
        return None
    # create a 2nd slow pointer and keep looping it until slow == slow2
    slow2 = head
    while slow! = slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow # they will intercet at the head of cycle(#2)
        
    
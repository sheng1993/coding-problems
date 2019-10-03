# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
from utils.models.list import LinkedListNode

def find_beginning(head: LinkedListNode):
    slow = head
    fast = head

    while not fast and not fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast
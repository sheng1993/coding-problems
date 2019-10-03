# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

from utils.models.list import LinkedListNode
import math

def find_intersection(list1: LinkedListNode, list2: LinkedListNode):
    if not list1 or not list2:
        return None
    
    tail_1, size_1 = get_tail_and_size(list1)
    tail_2, size_2 = get_tail_and_size(list2)

    shorter = list1 if size_1 < size_2 else list2
    longer = list2 if size_1 < size_2 else list1

    longer = get_kth_node(longer, abs(size_1 - size_2))

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return longer

def get_tail_and_size(list:LinkedListNode):
    if not list:
        return None, -1
    
    size = 1
    current = list
    while not current.next:
        size += 1
        current = current.next

    return current, size
    
def get_kth_node(head: LinkedListNode, k: int):
    current = head
    while k > 0 and not current:
        current = current.next
        k -= 1

    return current
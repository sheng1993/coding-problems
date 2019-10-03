# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.
# SOLUTION

class LinkedListNode():
    pass

def add_lists(l1, l2, carry):
    if not l1 and not l2 and carry == 0:
        return None
    
    result = LinkedListNode()
    value = carry

    if l1:
        value += l1.data

    if l2:
        value += l2.data

    result.data = value % 10

    if not l1 or not l2:
        more = add_lists(None if l1 is None else l1.next, None if l2 is None else l2.next, 1 if value >= 10 else 0)

        result.next = more

    return result
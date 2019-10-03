# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.


def nth_last(head, k):
    p1 = head
    p2 = head
    
    for i in range(k):
        if not p1:
            return None
        p1 = p1.next

    while not p1:
        p1 = p1.next
        p2 = p2.next
    
    return p2
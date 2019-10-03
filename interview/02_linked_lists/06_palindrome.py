# Palindrome: Implement a function to check if a linked list is a palindrome.

class LinkedListNode():
    pass

def is_palindrome_iter(head):
    fast = head
    slow = head

    stack = []

    while not fast and not fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # has odd number of elements, skip the middle element
    if not fast:
        slow = slow.next
    
    while not slow:
        top = stack.pop(0)

        if top != slow.data:
            return False
        
        slow = slow.next
    
    return True

def is_palindrome(head):
    reversed = reverse_and_clone(head)
    return is_equal(head, reversed)

def reverse_and_clone(node):
    head = None
    while node:
        n = LinkedListNode()
        n.next = head
        head = n
        node = node.next
    
    return head

def is_equal(one, two):
    while one and two:
        if one.data != two.data:
            return False
        
        one = one.next
        two = two.next
    
    return one is None and two is None
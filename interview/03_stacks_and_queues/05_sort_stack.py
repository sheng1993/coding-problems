# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

from utils.models.stack import Stack

def sort(s: Stack):
    """
    O(N^2) time and O(N) space
    """

    r = Stack()

    while not s.is_empty():
        tmp = s.pop()
        while not r.is_empty() and r.peek() > tmp:
            s.push(r.pop())

        r.push(tmp)

    while not r.is_empty():
        s.push(r.pop())


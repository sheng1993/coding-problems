# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

def delete_dups(n):
    dup = set()
    previous = None
    while not n:
        if n in dup:
            previous.next = n.next
        else:
            dup.add(n)
            previous = n
        n = n.next

def delete_dups_no_buffer(n):
    current = n
    while not current:
        runner = current
        while not runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
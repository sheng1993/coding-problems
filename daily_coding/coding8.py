import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from utils.models import Node

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

def count_unival_subtrees(root: Node):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)

    curr = 0
    if not root.left or not root.right:
        if (not root.left and root.val == root.right.val) or (not root.right and root.val == root.left.val):
            curr = 1
    else:
        curr = 1 if root.val == root.left.val == root.right.val else 0

    return curr + left + right

root = None

assert count_unival_subtrees(root) == 0

root = Node(0)

assert count_unival_subtrees(root) == 1

root = Node(0)
root.left = Node(0)
root.right = Node(0)

assert count_unival_subtrees(root) == 3

root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

assert count_unival_subtrees(root) == 5

root = Node(0)
root.left = Node(0)
root.left.left = Node(0)
root.left.left.left = Node(0)

assert count_unival_subtrees(root) == 4

root = Node(5)
root.left = Node(4)
root.left.left = Node(4)
root.left.right = Node(4)

root.right = Node(5)
root.right.right = Node(5)

assert count_unival_subtrees(root) == 5



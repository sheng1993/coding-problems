# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

from utils.models.trees import Node
from typing import List

def create_level_linked_list(root):
    result = []
    current = []

    if root:
        current.append(root)
    
    while current:
        result.append(current)
        parents: List[Node] = current
        current = []
        for parent in parents:
            if parent.left:
                current.append(parent.left)
            if parent.right:
                current.append(parent.right)

    return result
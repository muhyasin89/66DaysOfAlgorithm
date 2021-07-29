"""
UNSOLVED DATA
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


stack = []


def change_to_tree(
    root,
    a,
):
    curr = None
    while a:
        if a[0] == None:
            a.pop(0)

        if a[1] == None:
            a.pop(1)

        if a[0] != None and len(stack) % 2 == 0:
            curr.left = Node(a[0])
            curr = curr.left
        elif len(stack) % 2 == 1:
            curr.right = Node(a[0])
            curr = curr.right

        print(a)
        a.pop(0)
        change_to_tree(root, a)


a = [-10, 9, 20, None, None, 15, 7]
root = Node(a[0])
a.pop(0)
curr = None
change_to_tree(root, a)
import pdb

pdb.set_trace()

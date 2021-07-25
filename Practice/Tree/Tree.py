class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


"""
           7
          /   \
        5       8
      /   \    /  \
     4     3  9    10
"""


def setPerfectTree():
    root = Node(7)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(4)
    root.left.righ = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(10)

    return root


"""
            7
          /   \
        5       8
      /   \    /  \
     4     3  9    10
    /  \
    2   1
"""


def setCompleteTree():
    root = Node(7)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(3)
    root.left.left.left = Node(2)
    root.left.left.right = Node(1)
    root.right.left = Node(9)
    root.right.right = Node(10)

    return root


"""
            5
          /   \
        1       3
      /   \    /  \
     2     4  7     10
             /  \
            8    9
"""


def setPerfectTree():
    root = Node(5)
    root.left = Node(1)

    root.left.left = Node(2)
    root.left.right = Node(4)

    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(7)
    root.right.left.left = Node(8)
    root.right.left.right = Node(9)

    return root

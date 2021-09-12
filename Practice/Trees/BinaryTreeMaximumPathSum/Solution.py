import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode) -> int:

    record = -(math.inf)

    def traverse(node):
        # Reached end
        if node is None:
            print("This is Zero")
            return 0

        print("node.val", node.val)
        left = traverse(node.left)
        print("left", left)
        right = traverse(node.right)
        print("right", right)

        retval = max(node.val, node.val + left, node.val + right)
        print("retval", retval)
        potrecord = max(retval, node.val + left + right)
        print("potrecord", potrecord)

        nonlocal record
        if potrecord > record:
            record = potrecord
        print("record", record)
        print("=========")
        return retval

    traverse(root)
    return record


def example(root=None):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    return root


root = example()
maxPathSum(root)

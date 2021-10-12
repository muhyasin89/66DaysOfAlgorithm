class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortArrBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Tree(arr[mid])
    root.left = sortArrBST(arr[:mid])
    root.right = sortArrBST(arr[(mid + 1) :])

    return root


arr = [1, 4, 5, 6, 7]
first_tree = sortArrBST(arr)
first_tree

print("Array {}".format(arr))


def preOrder(head):
    if head == None:
        return

    print("{}".format(head.val), end=" ")
    preOrder(head.left)
    preOrder(head.right)


print("PreOrder Traversal - recursive solution : ")
preOrder(first_tree)


def inOrder(head):
    if head == None:
        return

    inOrder(head.left)
    print("{}".format(head.val), end=" ")
    inOrder(head.right)


print("\nInorder Traversal - recursive solution : ")
inOrder(first_tree)


def postOrder(head):
    if head == None:
        return

    postOrder(head.left)
    postOrder(head.right)
    print("{}".format(head.val), end=" ")


print("\nPost Order Traversal - recursive solution : ")
postOrder(first_tree)
print("\n")

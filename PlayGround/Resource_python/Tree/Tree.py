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


def preOrder(head):
    if head == None:
        return []

    left = preOrder(head.left)
    right = preOrder(head.right)

    return [head.val] + left + right


print(preOrder(first_tree))


def inOrder(head):
    if head == None:
        return []

    left = inOrder(head.left)
    right = inOrder(head.right)

    return left + [head.val] + right


print(inOrder(first_tree))


def postOrder(head):
    if head == None:
        return []

    left = postOrder(head.left)
    right = postOrder(head.right)

    return left + [head.val] + right


print(postOrder(first_tree))

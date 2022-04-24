class Tree:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left

        self.right = right

def sortArrBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Tree(arr[mid])
    root.left = sortArrBST(arr[:mid])
    root.right = sortArrBST(arr[(mid+1):])

    return root

#arr -> tree 
arr = [1,4,5,6,7]
first_tree = sortArrBST(arr)

# preorder
def preOrder(head):
    if head == None:
        return

    print("{} ".format(head.val), end="")
    preOrder(head.left)
    preOrder(head.right)

print("PreOrder Transversal")
preOrder(first_tree)

# in order
def inOrder(head):
    if head == None:
        return 

    inOrder(head.left)
    print("{} ".format(head.val), end="")
    inOrder(head.right)

print("\nInOrder Transversal")
inOrder(first_tree)

# post order
def PostOrder(head):
    if head == None:
        return 

    PostOrder(head.left)
    PostOrder(head.right)
    print("{} ".format(head.val), end="")
    

print("\nPostOrder Transversal")
PostOrder(first_tree)
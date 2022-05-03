class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def changeIntoTree(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = changeIntoTree(arr[:mid])
    root.right = changeIntoTree(arr[mid+1:])

    return root

nodes = [1,2,3,4, 6,7,9]

tree = changeIntoTree(nodes)


def printLeafNodes(root: Node):
    if(not root):
        return

    if(not root.left and not root.right):
        print(root.val, end=" ")

    if root.left:
        printLeafNodes(root.left)

    if root.right:
        printLeafNodes(root.right)

printLeafNodes(tree)


def calculateBranchSum(root, sum_result, sum_list):
    if not root:
        return

    sum_result = sum_result+ root.val

    if not root.left and not root.right:
        sum_list.append(sum_result)

    calculateBranchSum(root.left, sum_result, sum_list)
    calculateBranchSum(root.right, sum_result, sum_list)
    
def brachSum(root):
    sum_list = []
    calculateBranchSum(root, 0, sum_list)

    return sum_list

print(brachSum(tree))
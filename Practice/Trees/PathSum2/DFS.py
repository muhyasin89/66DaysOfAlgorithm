from typing import List


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Tree, targetSum: int) -> List[List[int]]:
    if not root:
        return []
    ans = []
    stack = [(root, [root.val], root.val)]  # (node, path, sum)
    while stack:
        node, path, Sum = stack.pop()
        # path found
        if not node.left and not node.right and Sum == targetSum:
            ans.append(path)

        
        # recursion
        if node.left:
            stack.append(
                (node.left, path + [node.left.val], Sum + node.left.val)
            )
        if node.right:
            stack.append(
                (node.right, path + [node.right.val], Sum + node.right.val)
            )

        print("Inside complete stack: {} ans: {}".format(stack, ans))
    return ans


if __name__ == "__main__":
    sum = 22

    root = Tree(5)
    root.left = Tree(4)
    root.left.left = Tree(11)
    root.left.left.left = Tree(7)
    root.left.left.right = Tree(2)

    root.right = Tree(8)
    root.right.left = Tree(13)
    root.right.right = Tree(4)
    root.right.right.left = Tree(5)
    root.right.right.right = Tree(1)

    pathSum(root, sum)

    print("Expected Result:{}".format([[5, 4, 11, 2], [5, 8, 4, 5]]))

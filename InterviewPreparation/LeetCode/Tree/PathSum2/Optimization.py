from typing import List


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Tree, targetSum: int) -> List[List[int]]:
    # base cases
    if not root:
        return []
    if not root.left and not root.right and targetSum == root.val:
        return [[root.val]]

    ans = []
    subpath = pathSum(root.left, targetSum - root.val) + pathSum(
        root.right, targetSum - root.val
    )
    # print("Inside complete subpath: {}".format(subpath))
    for path in subpath:
        ans.append([root.val] + path)
    print("Inside complete subpath: {} ans: {}".format(subpath, ans))
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

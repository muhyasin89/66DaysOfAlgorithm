class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, sum, cur, ret):
    new_ret = []
    if root == None:
        return

    cur.append(root.val)
    if root.left == None and root.right == None and root.val == sum:
        new_ret = cur
        ret.append(new_ret)

    print("Inside complete cur:{} ret: {}".format(cur, ret))
    pathSum(root.left, sum - root.val, cur, ret)
    pathSum(root.right, sum - root.val, cur, ret)

    cur.pop()  # remove last element in cur list and it destroy everything


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

    ret = []
    cur = []
    pathSum(root, sum, cur, ret)
    print("Expected Result:{}".format([[5, 4, 11, 2], [5, 8, 4, 5]]))
    # [[5,4,11,2],[5,8,4,5]]

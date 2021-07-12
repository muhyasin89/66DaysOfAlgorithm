def height(root):
    if root == None:
        return -1
    # divide and conquer
    depth_left = height(root.left)
    depth_right = height(root.right)
    depth = max(depth_left, depth_right) + 1
    # return the final result
    return depth

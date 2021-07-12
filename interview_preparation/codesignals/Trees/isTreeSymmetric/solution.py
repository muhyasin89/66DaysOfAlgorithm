def isTreeSymmetric(t):
    def mirrorEquals(left, right):
        if left is None or right is None:
            return left == None and right == None
        return (
            left.value == right.value
            and mirrorEquals(left.left, right.right)
            and mirrorEquals(left.right, right.left)
        )

    return mirrorEquals(t, t)

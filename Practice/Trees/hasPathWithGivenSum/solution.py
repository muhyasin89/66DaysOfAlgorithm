#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    # if no tree node and s is 0
    if t is None:
        if s == 0:
            return True
        else:
            return False
    else:
        # check if 2 tree has value

        if t.left is not None and t.right is not None:
            # The any() function returns True if any element of an iterable is True.
            # If not, any() returns False.
            return any(
                [
                    hasPathWithGivenSum(t.left, s - t.value),
                    hasPathWithGivenSum(t.right, s - t.value),
                ]
            )
        elif t.left is not None:
            return hasPathWithGivenSum(t.left, s - t.value)
        elif t.right is not None:
            return hasPathWithGivenSum(t.right, s - t.value)
        else:
            if t.value == s:
                return True
            else:
                return False

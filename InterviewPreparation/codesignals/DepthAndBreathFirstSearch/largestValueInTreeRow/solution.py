#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
import math


def largestValuesInTreeRows(t):
    if t is None:
        return []
    stack = [t]
    result = []
    while len(stack) > 0:
        result.append(max(tree.value for tree in stack))
        next_row = [tree.left for tree in stack if tree.left] + [
            tree.right for tree in stack if tree.right
        ]
        stack = next_row
    return result

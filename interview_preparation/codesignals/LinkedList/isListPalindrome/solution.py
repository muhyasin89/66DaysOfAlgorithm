# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):

    # Temp pointer
    slow = l

    # Declare a stack
    stack = []

    ispalin = True

    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.value)

        # Move ahead
        slow = slow.next

    # Iterate in the list again and
    # check by popping from the stack
    while l != None:

        # Get the top most element
        i = stack.pop()

        # Check if data is not
        # same as popped element
        if l.value == i:
            ispalin = True
        else:
            ispalin = False
            break

        # Move ahead
        l = l.next

    return ispalin

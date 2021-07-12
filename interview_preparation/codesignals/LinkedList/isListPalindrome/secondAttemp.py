# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):

    temp = l

    stack = []
    isPalindrome = True

    # input all list to array
    while temp != None:
        stack.append(temp.value)
        temp = temp.next

    # find palindrom by compairing from tail to first

    while temp != None:
        i = stack.pop()  # indexing from behind

        if temp.value == i:
            isPalindrome = True
        else:
            isPalindrome = False
            break
        # move ahead
        temp = temp.next

    return isPalindrome

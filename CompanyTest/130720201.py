# Note: Proper indentation is required
# Click HELP above to see examples of handling input/debug/output
# INPUT: n = input()
# DEBUG: print(n)
# OUTPUT: print(result)

# Write the code to solve the problem below,
# format the "result" as specified in the problem statement
# and finally, write the result to stdout
# IMPORTANT: Remove all debug statements for final submission


# goal check if character or sting after # is same(case sensitif)

# step 1 find how to identify #
# step 2 remove front string and keep back string of #
# step 3 compare 2 of them

# question what happen if 2#334#4 there will be 3 if split
# take last one? and compare to another one

# whether string are equals? means same length, same end character?or there are any other parameter?
n = input()
n1 = input()


def split_string(n):
    return n.split("#")


def get_list(after_sharp):

    last = after_sharp[len(after_sharp) - 1]
    return last
    # if last:
    #     return last
    # else:
    #     if len(after_sharp):
    #         after_sharp.pop()
    #         return get_list(after_sharp)
    #     else:
    #         return None #false because it will compare to char


# what happen if # in last


def result(n, n1):
    n_last = get_list(split_string(n))
    n1_last = get_list(split_string(n1))
    # print(n_last,n1_last)
    # case sensitif? and equals in length
    if n_last == n1_last and len(split_string(n)) == len(split_string(n1)):
        return True
        # does any other list should be compare?
        # def compare_list(a, b):
        #     for i in range(len(a)-1): #both of list is equals
        #         if a[i] == b[i]:
        #             return True
        #         else:
        #             return False
        #             break
        # compare_list(split_string(n), split_string(n1))
    # if n_last == n1_last:
    # return True
    else:
        return False


print(result(n, n1))

# can i see hidden test, i dont know whats wrong

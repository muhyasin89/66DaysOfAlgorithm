import re

line = "def      m   e  gaDifficu     ltFun        ction(x):"
"""
    the easy way but failed
"""
# def catWalk(code):
#     return re.sub(' +', ' ', code)

# def catWalk(code):
#     #change string into list
#     code = code.split(" ")
#     #find all index which has space
#     list_index = [i for i, x in enumerate(code) if x == ""]

#     #sort from bigger number to sort number
#     list_index = sorted(list_index, reverse=True)

#     #remove all space in code
#     for item in list_index:
#         code.pop(item)

#     #remove first list from the rest
#     new_code = code[1:]

#     #add space in front af element
#     new_code = [' {}'.format(x) for x in new_code]

#     #put back first element
#     new_code.insert(0,code[0])

#     result = ''
#     #change list into string
#     for ele in new_code: 
#         result += ele  

#     return result




"""
Result from internet
"""

from functools import reduce

def catWalk(code):
    return reduce(lambda x,y:x+' '+y, [i for i in code.rsplit()])


print(catWalk(line))
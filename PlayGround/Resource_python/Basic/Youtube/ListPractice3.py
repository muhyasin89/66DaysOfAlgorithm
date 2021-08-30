from itertools import combinations

arr = ["ar1r", "a", "fe2", "ef", "cc", "bb", "ba"]

# return combination that palindrome
# expected ["ar1r", "a", "fe2", "ef", "ba"]


# print(checkCombination(arr))


# practice 2
dict_arr = {"{": "}", "(": ")", "[": "]"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False


# print(checkClosure(inp_str))
# print(checkClosure(inp_str1))
# print(checkClosure(inp_str2) is False)
# print(checkClosure(inp_str3) is False)

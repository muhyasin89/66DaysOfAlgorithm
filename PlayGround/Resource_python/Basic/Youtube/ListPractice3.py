from itertools import combinations

arr = ["ar1r", "a", "fe2", "ef", "cc", "bb", "ba"]

# return combination that palindrome
# expected ["ar1r", "a", "fe2", "ef", "ba"]


def checkPalindrome(item):
    # change string to list
    list_item = list(item)
    mid = len(list_item) // 2

    left = list_item[:mid]
    right = list_item[mid:]

    if len(left) != len(right):
        right.pop(0)

    for i in range(len(left)):
        if left[i] != right[len(right) - i - 1]:
            return False

    return True


def checkCombination(arr):
    result_list = []
    list_combinations = list(combinations(arr, 2))

    for str1, str2 in list_combinations:
        # if item is palindrome add to result list
        str_item = str1 + str2
        if checkPalindrome(str_item):
            if str1 not in result_list:
                result_list.append(str1)
            if str2 not in result_list:
                result_list.append(str2)

    return result_list


print(checkCombination(arr))


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

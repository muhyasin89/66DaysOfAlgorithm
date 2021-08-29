from itertools import combinations

arr = ["ar1r", "a", "fe2", "ef", "cc", "bb", "ba"]

# return combination that palindrome
# expected ["ar1r", "a", "fe2", "ef", "ba"]


def checkPalindrome(str1):
    list_str1 = list(str1)

    mid = len(list_str1) // 2
    left = list_str1[:mid]  # ['f', 'e',]
    right = list_str1[mid:]  # [ ''2', e', 'f'] ->pop-> [ 'e', 'f']

    if len(left) != len(right):
        right.pop(0)

    for i in range(len(left)):
        if left[i] != right[len(left) - i - 1]:
            return False

    return True


def checkCombination(arr):
    list_combinations = list(combinations(arr, 2))

    result_list = []

    for item1, item2 in list_combinations:
        str_result = item1 + item2
        # check palindrome
        # if palindrome append ke result list
        if checkPalindrome(str_result):
            if item1 not in result_list:
                result_list.append(item1)
            if item2 not in result_list:
                result_list.append(item2)

    return result_list


# print(checkCombination(arr))


# practice 2
dict_arr = {"{": "}", "(": ")", "[": "]"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False


def removeCompleteClosure(list_str1):
    list_result = []
    for i in range(0, len(list_str1)):
        if list_str1[i] in dict_arr.values() and i >= 1:
            if list_str1[i - 1] in dict_arr.keys():
                if dict_arr[list_str1[i - 1]] != list_str1[i]:
                    return False
                else:
                    list_result.pop(len(list_result) - 1)
            else:
                list_result.append(list_str1[i])
        else:
            list_result.append(list_str1[i])

    return list_result


def checkClosure(inp):
    list_str = list(inp)

    if len(list_str) == 0:
        return True

    if len(list_str) % 2 != 0:
        return False

    mid = len(list_str) // 2
    left = list_str[:mid]
    right = list_str[mid:]

    left = removeCompleteClosure(left)
    right = removeCompleteClosure(right)

    print("{}: {}".format(left, right))
    if not left or not right:
        return False

    for i in range(len(left)):
        if left[i] in dict_arr.values():
            return False

        if dict_arr[left[i]] != right[len(right) - i - 1]:
            return False
    return True


print(checkClosure(inp_str))
print(checkClosure(inp_str1))
print(checkClosure(inp_str2) is False)
print(checkClosure(inp_str3) is False)

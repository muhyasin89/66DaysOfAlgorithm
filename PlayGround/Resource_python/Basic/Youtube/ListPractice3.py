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


def validClosure(list_pair):
    list_result = []
    if len(list_pair) == 1:
        return False

    for i in range(len(list_pair)):
        if list_pair[i] in dict_arr.values() and i < 1:
            return False
        else:
            if (
                list_pair[i] in dict_arr.values()
                and list_pair[i - 1] in dict_arr.keys()
            ):
                if dict_arr[list_pair[i - 1]] != list_pair[i]:
                    return False
                else:
                    list_result.pop(-1)
            else:

                list_result.append(list_pair[i])

    if len(list_result):
        validClosure(list_result)

    return True


def checkClosure(inp):
    list_inp = list(inp)

    return validClosure(list_inp)


print(checkClosure(inp_str))
print(checkClosure(inp_str1))
print(checkClosure(inp_str2) is False)
print(checkClosure(inp_str3) is False)

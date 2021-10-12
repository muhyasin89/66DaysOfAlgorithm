from itertools import combinations

arr = [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
# result 17 <-arr 1


def checkCombination(arr):
    dict_list = {}
    list_combinasi = list(combinations(arr, 2))

    for item1, item2 in list_combinasi:
        sum = item1 + item2
        if sum in dict_list.keys():
            dict_list[sum].append(item1)
            dict_list[sum].append(item2)
        else:
            dict_list[sum] = [item1, item2]

    str_result = ""
    list_result = dict_list[arr[0]]
    for i in range(len(list_result)):
        if i % 2 == 0:
            str_result = "{} {}".format(str_result, list_result[i])
        else:
            str_result = "{}, {}".format(str_result, list_result[i])

    return str_result


print(checkCombination(arr))
# 6, 11 10, 7 15,2

from itertools import combinations

arr = [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
# result 17 <-arr 1


def checkCombination(arr):
    list_combiantions = list(combinations(arr, 2))

    dict_list = {}
    for item1, item2 in list_combiantions:
        sum_item = item1 + item2
        if sum_item in dict_list.keys():
            dict_list[sum_item].append(item1)
            dict_list[sum_item].append(item2)
        else:
            dict_list[sum_item] = [item1, item2]

    return dict_list


result = checkCombination(arr)[arr[0]]
string_result = ""
for i in range(0, len(result)):
    if i % 2 == 0:
        string_result = "{} {}".format(string_result, result[i])
    else:
        string_result = "{}, {}".format(string_result, result[i])

print(string_result)
# 6, 11 10, 7 15,2

# hashmap count

from itertools import combinations

arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]


def checkDuplicate(arr):
    dict_list = {}
    for i in arr:
        if i not in dict_list.keys():
            dict_list[i] = 1
        else:
            dict_list[i] += 1

    for key, value in dict_list.items():
        print("nomor {}: {} kali".format(key, value))


checkDuplicate(arr)

# combination sum

arr1 = [1, 2, 3, 4, 5, 6, 7]
n = 8


def checkSum(arr, n):
    combinations_list = list(combinations(arr, 2))

    result_list = []

    for item1, item2 in combinations_list:
        if item1 + item2 == n:
            result_list.append(item1)
            result_list.append(item2)

    return result_list


print(checkSum(arr1, n))

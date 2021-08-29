from itertools import combinations

arr = [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]


def ArrayChallenge(arr):
    list_combinations = []
    result_dict = {}
    # code goes here

    for item in combinations(arr, 2):
        list_combinations.append(item)
        sum_list = item[0] + item[1]
        if (item[0] + item[1]) not in result_dict.keys():
            result_dict[list_combinations] = [item[0], item[1]]
        else:

            if item[0] not in result_dict[sum]:
                result_dict[sum_list].append(item[0])
            if item[1] not in result_dict[sum]:
                result_dict[sum_list].append(item[1])

    return result_dict[arr[0]]


# keep this function call here
print(ArrayChallenge(arr))

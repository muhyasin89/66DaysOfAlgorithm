# hashmap count

from itertools import combinations

arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
# expected answer
# number 1 :  3 time

# dict_number = {}
# for i in arr:
#     if i not in dict_number.keys():
#         dict_number[i] = 1
#     else:
#         dict_number[i] += 1

# for key, value in dict_number.items():
#     print("number {}: {} times".format(key, value))

# combination sum
arr1 = [1, 2, 3, 4, 5, 6, 7]
n = 8

combination_list = list(combinations(arr1, 2))
result_list = []
for item1, item2 in combination_list:
    if item1 + item2 == n:
        result_list.append(item1)
        result_list.append(item2)

print(result_list)

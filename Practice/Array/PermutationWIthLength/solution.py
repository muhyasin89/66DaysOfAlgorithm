from itertools import permutations

arr = [1, 2, 3, 4, 5]
L = 2

result_arr = []
for item in permutations(arr, L):
    result_arr.append(list(item))


print(result_arr)

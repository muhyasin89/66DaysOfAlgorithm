from itertools import permutations

arr = [1, 2, 3, 4, 5]

arr_perm = []
for item in permutations(arr, 2):
    arr_perm.append(list(item))

print(arr_perm)

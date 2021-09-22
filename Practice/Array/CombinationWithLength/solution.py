from itertools import combinations

arr = [1, 2, 3, 4, 5]
new_arr = []

for item in combinations(arr, 2):
    new_arr.append(item)

print(new_arr)

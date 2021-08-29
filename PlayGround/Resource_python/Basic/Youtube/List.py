# a = "Hello World"
# b = 342561

# list_a = a.split(" ")
# print(list_a)

# list_c = list(list_a[0])
# print(list_c)

# list_c.pop(2)
# print(list_c)

# list_c[1], list_c[2] = list_c[2], list_c[1]
# print(list_c)

# mid = len(list_c) // 2
# left = list_c[:mid]
# right = list_c[mid:]

# print(left)
# print(right)

# string_c = "".join(list_c)
# print(string_c)

# list_b = [int(i) for i in str(b)]
# print(list_b)

# list_b.sort()
# print(list_b)
# list_b.sort(reverse=True)
# print(list_b)


# from itertools import combinations, combinations_with_replacement, permutations

# print("============================")
# for item_a in permutations([1, 2, 3], 2):
#     print(item_a)

# print("============================")
# for item_b in combinations([1, 2, 3], 2):
#     print(item_b)

# print("============================")
# for item_c in combinations_with_replacement([1, 2, 3], 2):
#     print(item_c)


dict_list = {"{": "}", "[": "]", "(": ")"}


print("{" in dict_list.keys())
print("}" in dict_list.values())


for key, value in dict_list.items():
    print("ini key {}: ini value {}".format(key, value))

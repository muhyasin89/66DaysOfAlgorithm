# make string "Hello World" and string "11223344"
a = "Hello World"
b = "11223344"


# turn string into list
# list_a = a.split(" ")
list_a = list(a)
print(list_a)

# turn list int into list

# turn list into string
string_c = "".join(list_a)
print(string_c)

# swap list
list_a[1], list_a[2] = list_a[2], list_a[1]
print(list_a)

# make another list

# merge 2 list with same type

# check if 'k' inside list

# check index space
index_space = list_a.index(" ")
# remove duplicate

# remove space in list
list_a.pop(index_space)
print(list_a)

# cut list into 2 left and right
mid = len(list_a) // 2
left = list_a[:mid]
right = list_a[mid:]

print(left)
print(right)

# make hash map
dict_list = {"{": "}", "[": "]", "(": ")", "<": ">"}


print("{" in dict_list.keys())
print("}" in dict_list.values())


for key, value in dict_list.items():
    print("ini key {}: ini value {}".format(key, value))

# check if n in keys

# check if n in values

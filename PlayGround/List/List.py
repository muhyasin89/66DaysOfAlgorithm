# make string "Hello World" and string "1122334455"
str1 = "Hello World"
int1 = "1122334455"

print("Str: {} Int:{}".format(str1, int1))

# turn string into list
list_str = list(str1)
list_int = list(int1)

print("Str: {} Int:{}".format(list_str, list_int))

# turn list string into list int
list_int = [int(x) for x in list_int]
print(list_int)

# turn list into string
print("".join(list_str))

# remove duplicate
list_int = list(set(list_int))
print(list_int)

# check if 'space' inside list
print(" " in list_str)

# check index space
ind_space = list_str.index(" ")
print(ind_space)

# remove space in list
list_str.pop(ind_space)
print(list_str)

# swap list
list_str[4], list_str[5] = list_str[5], list_str[4]
print(list_str)

# make another list
list_int1 = [6, 7, 8, 9, 10]

# merge 2 list with same type
list_int = list_int + list_int1
print(list_int)

# cut list into 2 left and right
mid = len(list_str) // 2
left = list_str[:mid]
right = list_str[mid:]

print(left, right)

# make hash map
hash_map = {1: "first", 2: "second", 3: "third"}

# check if n in keys
print(1 in hash_map.keys())

# get hash_map get value of k
print(hash_map[1])

# check if n in values
print("third" in hash_map.values())

# itterate hashmap
for key, val in hash_map.items():
    print("{} = {} ".format(key, val))
# make string "Hello World" and string "11223344"
str1 = "Hello World"
int1 = "11223344"


print("Str: {} Int: {} ".format(str1, int1))
# turn string into list
list_str = list(str1)
print(list_str)

list_int = list(int1)
print(list_int)

# turn list string into list int
list_int = [int(x) for x in list_int]
print(list_int)

# turn list into string
print("".join(list_str))

# swap list
list_str[1], list_str[2] = list_str[2], list_str[1]
print(list_str)

# make another list
list_int1 = [6, 7, 8, 9, 10]

# merge 2 list with same type
list_int = list_int + list_int1
print(list_int)

# remove duplicate
list_int = list(set(list_int))
print(list_int)

# check if 'space' inside list
print("{}".format(" " in list_str))

# check index space
index_space = list_str.index(" ")
print(index_space)


# remove space in list
list_str.pop(index_space)
print(list_str)

# cut list into 2 left and right
mid = len(list_str) // 2
left = list_str[:mid]
right = list_str[mid:]

print(left)
print(right)

# make hash map
hash_map = {1: "first", 2: "second", 3: "third"}


# check if n in keys
print("1" in hash_map.keys())

# get hash_map get value of k
print(hash_map[1])

# check if n in values
print("third" in hash_map.values())

# itterate hashmap
for key, value in hash_map.items():
    print("ini key {}: ini value {}".format(key, value))

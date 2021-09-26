str1 = "abba"
string1 = "dog cat cat dog"
# result True

str2 = "abba"
string2 = "dog cat cat fish"
# return False


def areFollowingPattern(str1, string1):
    list_str = list(str1)
    list_string = string1.split(" ")

    hash_map = {}

    if len(list_str) != len(list_string):
        return False

    for i in range(len(list_str)):
        temp = list_str[i]
        if temp not in hash_map.keys():
            hash_map[temp] = list_string[i]
        else:
            if hash_map[temp] != list_string[i]:
                return False

    return True


print(areFollowingPattern(str1, string1))
print(areFollowingPattern(str2, string2))

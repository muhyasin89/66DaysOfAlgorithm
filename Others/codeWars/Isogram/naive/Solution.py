def is_isogram(string):
    # your code here
    string = string.lower()

    def convert(string):
        list = []
        list[:0] = string
        return list

    list_s = convert(string)
    if not list_s:
        return True

    for i in range(len(list_s)):
        curr = i
        for j in range(len(list_s) - 1):
            if (j + curr + 1) < len(list_s):
                if list_s[curr] == list_s[j + curr + 1]:
                    return False
    return True


print(is_isogram("Dermatoglyphics"))
# print(is_isogram("aba"))

# print(is_isogram("moOse"))

dict_map = {"{": "}", "[": "]", "(": ")", "<": ">"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  # expected True


def ValidBracket(str1, dict_map):
    list_str = list(str1)
    list_bracket = []

    for i in range(len(list_str)):
        if list_str[i] in dict_map.values() and i < 1:
            return False
        elif list_str[i] in dict_map.keys():
            list_bracket.append(list_str[i])
        elif list_str[i] in dict_map.values():
            if dict_map[list_bracket[-1]] != list_str[i]:
                return False
            else:
                list_bracket.pop(-1)
    return True


print(ValidBracket(inp_str, dict_map))
print(ValidBracket(inp_str1, dict_map))
print(ValidBracket(inp_str2, dict_map))
print(ValidBracket(inp_str3, dict_map))
print(ValidBracket(inp_str4, dict_map))

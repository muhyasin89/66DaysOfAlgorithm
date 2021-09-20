dict_map = {"{": "}", "[": "]", "(": ")", "<": ">"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  # expected True
inp_str5 = "{\{\{\{"  # expected False


def ValidBracket(str1, dict_map):
    list_bracket = []
    list_str = list(str1)

    for i in range(len(list_str)):
        temp = list_str[i]
        if temp in dict_map.values() and i < 1:
            return False
        elif temp in dict_map.keys():
            list_bracket.append(temp)
        elif temp in dict_map.values():
            if dict_map[list_bracket[-1]] != temp:
                return False
            else:
                list_bracket.pop(-1)

    if len(list_bracket) > 0:
        return False

    return True


print(ValidBracket(inp_str, dict_map))
print(ValidBracket(inp_str1, dict_map))
print(ValidBracket(inp_str2, dict_map))
print(ValidBracket(inp_str3, dict_map))
print(ValidBracket(inp_str4, dict_map))
print(ValidBracket(inp_str5, dict_map))

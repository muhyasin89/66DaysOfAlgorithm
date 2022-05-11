def changeListOfString(string):
    #string jadi list character
    list_char = list(string)
    list_result = []
    
    for i in range(len(list_char)):
        if i % 2 == 0 or i == 0:
            list_result.append(list_char[i].upper())
        else:
            list_result.append(list_char[i])
    return ''.join(list_result)

def to_weird_case(string):
    list_result = []
    #cut string into list
    list_string = string.split(" ")
    #check index if % 2 == 0 make Uppercase
    # "ada","apa","test"    
    for item in list_string:
        list_result.append(changeListOfString(item))
    #combine string with space
    return ' '.join(list_result)


print(to_weird_case("This is a test"))
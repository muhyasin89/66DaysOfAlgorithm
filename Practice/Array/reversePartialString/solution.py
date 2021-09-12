a = [
    "I",
    " ",
    "d",
    "r",
    "i",
    "v",
    "e",
    " ",
    "w",
    "i",
    "t",
    "h",
    " ",
    "B",
    "o",
    "l",
    "t",
]


def change_input(in_text):
    str1 = "".join(in_text)
    list_str = str1.split(" ")
    for i in range(len(list_str)):
        list_str[i] = list_str[i][::-1]
    list_str = list(" ".join(list_str))

    return list_str


print(change_input(a))

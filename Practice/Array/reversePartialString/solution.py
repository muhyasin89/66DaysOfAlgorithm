a = "I drive with Bolt"
# expected "I drive with Bolt"
b = "Saya adalah Programmer"
# expected "ayaS halada remmargorP"


def change_input(in_text):
    str1 = "".join(in_text)
    list_str = str1.split(" ")
    for i in range(len(list_str)):
        list_str[i] = list_str[i][::-1]
    list_str = list(" ".join(list_str))

    return "".join(list_str)


print(change_input(list(a)))
print(change_input(list(b)))

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True


# print(is_isogram("Dermatoglyphics"))
# print(is_isogram("aba"))

print(is_isogram("moOse"))

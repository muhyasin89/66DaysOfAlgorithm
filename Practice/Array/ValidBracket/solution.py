dict_map = {"{": "}", "[": "]", "(": ")", "<": ">"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  # expected True

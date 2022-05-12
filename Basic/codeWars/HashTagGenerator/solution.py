def generate_hashtag(s):
    #remove duplicate space
    s = s.split()
    if not len(s):
        return False
    
    s = " ".join(s)
    
    if len(s) > 140:
        return False
    #cut the string into list
    list_str = s.split(" ")
    if len(list_str) == 0:
        return False

    #make str with first of "#" and capitilize other
    list_str = [item.capitalize() for item in list_str]
    return "#" + "".join(list_str)

print(generate_hashtag("Do We have A Hashtag"))
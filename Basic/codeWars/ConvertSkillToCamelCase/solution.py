def to_camel_case(text):
    if "-" in text:
        words = text.split("-")
    else:
        words = text.split("_")

    for i in range(len(words)):
        if i !=0:
            words[i] = words[i].title()
        
    return ''.join(words)
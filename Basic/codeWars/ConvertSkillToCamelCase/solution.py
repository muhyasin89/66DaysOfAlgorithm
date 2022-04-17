def to_camel_case(text):
    text = text.replace("_","-")
    words = text.split("-")

    for i in range(len(words)):
        if i !=0:
            words[i] = words[i].title()
        
    return ''.join(words)
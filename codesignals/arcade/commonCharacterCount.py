
s1 = "aabcc"
s2 = "adcaa"

def commonCharacterCount(s1, s2):
    list_count = []

    #split all chacter into list
    list_s1 = list(s1)
    list_s2 = list(s2)

    #compare s1 to s2 O(n)
    for item_s1 in list_s1:
        #set variable to count the duplicate
        count = 0
        for item_s2 in list_s2:
            if item_s1 == item_s2:
                count+=1
        list_count.append(count)

    return max(list_count)



print(commonCharacterCount(s1, s2))

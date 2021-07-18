import collections

a = [2,1,3,5,3,2]

def get_duplicate(a):

    list_item =  [item for item, count in collections.Counter(a).items() if count > 1]

    list_result = list_item if(len(list_item) > 0) else -1
    if list_result is not -1:
        final_value = list_result[0] if(len(list_result) == 1) else list_result
    else:
        final_value = list_result
    return final_value

def get_second_index(duplicate_list):
    second_index = []
    for item in duplicate_list:    
        check_duplicate = [i for i, x in enumerate(a) if x == item]
        if type(check_duplicate) is list:
            if len(check_duplicate) > 0:
                second_index.append(check_duplicate[-1])

    return second_index

def firstDuplicate(a):
    duplicate_list = get_duplicate(a)
    if type(duplicate_list) is not list:
       final_value =  duplicate_list
    else:
        second_index =get_second_index(duplicate_list)
        if len(second_index) > 0:
            final_value = a[min(second_index)]
        else:
            final_value = a[duplicate_list]
    #get first duplicate
    return final_value

print(firstDuplicate(a))


def sortByHeight(a):
    #get index of not -1
    list_index = []
    list_value = []
    i=0
    
    #store value and list index
    for item in a:
        if item != -1:
            list_index.append(i)
            list_value.append(item)
            
        i+=1
        
    list_value.sort()
    
    j=0
    #put the value to original place
    for item in list_value:
        a[list_index[j]] = item
        j+=1
        
    return a

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))
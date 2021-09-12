
def reverse(llist):
    # Write your code here
    temp = llist
    position = llist
    
    while(temp!= None):
        prev = temp.prev
        temp.prev = temp.next
        temp.next = prev
        position = temp
        temp = temp.prev
        
    return position

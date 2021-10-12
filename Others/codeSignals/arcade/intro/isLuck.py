

def isLucky(n):
    res = [int(x) for x in str(n)]
    equal = True

    if len(res) % 2 == 0:
        second_half = int(len(res)/2)
    else:
        second_half = int((len(res) -1)/2 + 2)
        equal = False
        
    if equal and sum(res[:second_half]) == sum(res[second_half:]):
        return True
    else:
        return False


print(isLucky(134008))
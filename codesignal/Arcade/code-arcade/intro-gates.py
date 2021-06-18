#given 2 digit ex: 43
#break it into '4' and '3'
#and sum it 4+3

def addTwoDigits(n):
    list_int = [int(a) for a in str(n)]
    return sum(list_int)

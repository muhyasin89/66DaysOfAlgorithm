import math

def is_square(n):
    if(n>=0):
        result = math.sqrt(n)
        
        if(result*result == n):
            return True
    
    return False # fix me
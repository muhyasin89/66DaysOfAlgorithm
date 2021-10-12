

def maxMultiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    else:
        return bound - (bound % divisor)


print(maxMultiple(7, 100))
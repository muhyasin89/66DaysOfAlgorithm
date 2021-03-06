a = 808

def lateRide(n):

    hour = n // 60
    minute = n % 60

    digit_string = str(hour) + str(minute)

    digit_map = map(int, digit_string)

    return sum(digit_map)
    

print(lateRide(a))

#more effective 
def lateRide(n):
    return sum(map(int, str(n // 60 * 100 + n % 60)))
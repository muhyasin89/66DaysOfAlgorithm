def digital_root(n):
    if int(n) < 10:
       return n
    else:
        res = [int(x) for x in str(n)]
        print(res)
        result = 0
        for i in res:
            result += i
        return digital_root(result)

        


print(digital_root(132189))
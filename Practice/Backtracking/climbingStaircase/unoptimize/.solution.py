def climbingStaircase(n, k):
    final_res = []

    def CSR(n, k, res):
        result = []
        if n == 0:
            final_res.append(res)
        else:
            for i in range(1, k + 1):
                if n - i >= 0:
                    CSR(n - i, k, res + [i])

    final_res.append(CSR(n, k, []))
    res = [i for i in final_res if i]  # remove None
    if res == []:
        res = [[]]

    return res

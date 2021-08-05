import math


def phoneCall(min1, min2_10, min11, s):
    min_call = []
    if s < min1:
        return 0
    s_cost = s - min1

    min_call.append(1)
    if s_cost > 9:
        s_cost = s_cost - (9 * min2_10)

        min_call.append(9)
        if s_cost > 0:
            s_cost = math.floor(s_cost / min11)
            min_call.append(s_cost)
    else:
        s_cost = abs(s_cost // min2_10)
        min_call.append(s_cost)

    return sum(min_call)


# more effective solution
# def phoneCall(min1, min2_10, min11, s):
#     if s < min1:
#         return 0
#     elif s >= min1 and s <= min1 + 9 * min2_10:
#         return 1 + (s - min1) // min2_10
#     return 10 + (s - min1 - 9 * min2_10) // min11

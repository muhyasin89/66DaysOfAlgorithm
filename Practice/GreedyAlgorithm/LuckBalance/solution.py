def luckBalance(k, contests):
    # Write your code here
    contests.sort(reverse=True)
    luck = 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]

    return luck

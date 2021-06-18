# Enter your code here. Read input from STDIN. Print output to STDOUT

# n=int(input())
# lst=list(map(int, input().split()))
n=10
lst=[64630,11735,14216,99233,14470,4978,73429,38120,51135,67060]

import statistics
# from collections import Counter

def mean(lst):
    # return int(sum(lst)/n)
    return statistics.mean(lst)


def median(lst):
    # sort_x = x.sort()
    # if((n%2) != 1):
    #     middle_x = int(n/2)
    #     return int(sort_x[middle_x-1] + sort_x[middle_x])/2
    return statistics.median(lst)


def mode(lst):
    pass

    # try:
    #     return statistics.mode(lst)
    # except:
    #     lst_count = [x for x in set(lst) if lst.count(x) > 1]
    #     return min(lst_count)


    # data = Counter(lst)
    # if(len(data.most_common()) > 1):
    #     mode = min(set(lst))
    # else:
    #     mode = data.most_common()
    #
    # return mode




print(mean(lst, n))
print(median(lst, n))
print(mode(lst))

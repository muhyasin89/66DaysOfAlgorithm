import random


def random_list(n):
    list_n = []
    for i in range(n):
        list_n.append(random.randint(1, 20))

    return list_n


n = 10
arr = random_list(n)

print(arr)

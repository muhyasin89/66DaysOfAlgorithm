arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
# expected answer
# number 1 :  3 time
hash_map = {}


def sumList(arr, hash_map):
    for item in arr:
        if item in hash_map.keys():
            hash_map[item] += 1
        else:
            hash_map[item] = 1

    return hash_map


def printHashMap(hash_map):
    for key, val in hash_map.items():
        print("number: {} = {} times".format(key, val))


hash_map = sumList(arr, hash_map)

printHashMap(hash_map)

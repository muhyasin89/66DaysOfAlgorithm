


def printAll(i, arr, permutation):
    print("i is {}".format(i))
    print("array is {}".format(arr))
    print("pemutation {}".format(permutation))

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def permutationHelper(i, array, permutation):
    if i == len(array):
        print("last index {} array {} slice array {}".format(i, array, array[:]))
        permutation.append(array[:])

    else:
        for j in range(i, len(array)):
            print("== before first swap ==")
            printAll(i, array, permutation)
            swap(i, j, array)

            print("== after first swap ==")
            printAll(i, array, permutation)
            permutationHelper(i+1, array, permutation)

            print("== after being pemutation ==")
            printAll(i, array, permutation)

            swap(i, j, array)
            print("== after second swap ==")
            printAll(i, array, permutation)

            print("================================")


def getPermutation(array):
    permutation = []
    permutationHelper(0, array, permutation)
    print("final permutations: {}".format(permutation))
    return permutation


getPermutation([1,2,3])

a = [2, 1, 4, 5, 1]

a.sort()
print(a)

a.sort(reverse=True)
print(a)

from itertools import combinations, combinations_with_replacement, permutations

a = permutations([1, 2, 3], 2)

for item in a:
    print(item)

print("=======================")

b = combinations([1, 2, 3], 2)

for item in b:
    print(item)

print("=======================")

c = combinations_with_replacement([1, 2, 3, 4], 2)

for item in c:
    print(item)


print("=======================")

list1 = ["a", "b", "c"]
list2 = [1, 2]
all_combinations = []

list1_permutations = permutations(list1, len(list2))


for each_permutation in list1_permutations:
    zipped = zip(each_permutation, list2)
    all_combinations.append(list(zipped))

print(all_combinations)

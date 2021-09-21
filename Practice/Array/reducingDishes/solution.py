from typing import List

satisfaction = [-1, -8, 0, 5, -9]  # input
output = 14  # Output: 14

satisfaction1 = [4, 3, 2]  # input
output1 = 20  # Output: 20

satisfaction2 = [-1, -4, -5]  # input
output2 = 0  # Output: 0


def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort(reverse=True)
    while sum(satisfaction) < 0:
        satisfaction.pop()

    total = 0
    l = len(satisfaction)
    for i in range(l):
        total += satisfaction[i] * (l - i)
    return total


print(maxSatisfaction(satisfaction) == output)
# print(maxSatisfaction(satisfaction1) == output1)
# print(maxSatisfaction(satisfaction2) == output2)

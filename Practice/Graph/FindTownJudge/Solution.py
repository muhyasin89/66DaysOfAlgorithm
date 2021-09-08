import collections


def findJudge(n, trust):

    # Condition 1
    cannidates = set(range(1, n + 1)) - set([i[0] for i in trust])

    # Condition 2
    counts = collections.Counter()
    for a, b in trust:
        counts[b] += 1

    # Greedy
    for i in cannidates:
        if counts[i] == n - 1:
            return i

    return -1


if __name__ == "__main__":
    # n = 2
    # trust = [[1, 2]]

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]

    print(findJudge(n, trust))

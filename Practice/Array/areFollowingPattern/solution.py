def areFollowingPatterns(strings, patterns):
    return (
        len(set(strings))
        == len(set(patterns))
        == len(set(zip(strings, patterns)))
    )

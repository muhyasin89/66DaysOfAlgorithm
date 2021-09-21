ransomNote = "a"
magazine = "b"
# expected False

ransomNote1 = "aa"
magazine1 = "ab"
# expected False

ransomNote2 = "aa"
magazine2 = "aab"
# expected True


def canConstruct(ransomNote: str, magazine: str) -> bool:

    for c in set(ransomNote):
        if ransomNote.count(c) > magazine.count(c):
            return False
    return True


print(canConstruct(ransomNote, magazine))
print(canConstruct(ransomNote1, magazine1))
print(canConstruct(ransomNote2, magazine2))

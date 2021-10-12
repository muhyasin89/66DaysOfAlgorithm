inputArray = ["aba", "aa", "ad", "vcd", "aba"]


def allLongestStrings(inputArray):
    longest_string = max(inputArray, key=len)
    print(longest_string)
    new_item = []
    for item in inputArray:
         if len(item) == len(longest_string):
             new_item.append(item)
    
    return new_item

print(allLongestStrings(inputArray))
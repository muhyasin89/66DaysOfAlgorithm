
# s1 = "aabcc"
# s2 = "adcaa"

s1 = "abca"
s2 = "xyzbac"

# s1="zzzz"
# s2="zzzzzzz"

# def commonCharacterCount(s1, s2):
#     # find from s1 as based the duplicate character
#     dict_count = {}

#     for char in s1:
#         counts=s1.count(char)
#         if counts > 1 or char in s2:
#             dict_count[char] = counts
            
#     for char in s2:
#         counts = s2.count(char)
#         if char in dict_count.keys() and dict_count[char] > counts:
#             dict_count[char] = counts
                
#     return sum(dict_count.values())

#the result is

def commonCharacterCount(s1, s2):
    #remove duplicate s1
    s1_set = set(s1)
    result = 0

    #count s1 set and count from both s1 and s2
    for letter in s1_set:
        s1_count = s1.count(letter)
        s2_count = s2.count(letter)
        #result from min of char count
        result += min([s1_count, s2_count])
    return result

print(commonCharacterCount(s1, s2))

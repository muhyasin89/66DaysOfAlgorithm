str1 = "abba"
string1 ="dog cat cat dog"
# result True


str2 =  "abba"
string2 ="dog cat cat fish"

def checkFollowingPattern(s, str)
    hash_map = {}
    list_s = s.split("")
    list_str = str.split(" ")

    if list_s.length != list_str.length
        return false
    end

    for i in 0..list_s.length
        if hash_map.key?(list_s[i])
            if hash_map[list_s[i]] != list_str[i]
                return false
            end
        else
            hash_map[list_s[i]] = list_str[i]
        end
    end

    return true
end

puts checkFollowingPattern(str1, string1)
puts checkFollowingPattern(str2,string2)

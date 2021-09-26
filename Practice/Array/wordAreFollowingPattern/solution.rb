str1 = "abba"
string1 ="dog cat cat dog"
# result True


str2 =  "abba"
string2 ="dog cat cat fish"


def areFollowingPattern(str1,string1)
    hash_map ={}
    list_str = str1.split("")
    list_string = string1.split(" ")

    if list_str.length != list_string.length
        return false
    end

    for i in 0..list_str.length
        temp = list_str[i]
        if hash_map.key?(temp)
            if hash_map[temp] != list_string[i]
                return false
            end
        else
            hash_map[temp] = list_string[i]
        end
    end

    return true
end

puts areFollowingPattern(str1,string1)
puts areFollowingPattern(str2,string2)
string1 = "abba"
str1 = "dog cat cat dog"
# result True

string2 = "abba"
str2 = "dog cat cat fish"


def areFollowingPatterns(s, str)
    dict_map = {}
    list_s = s.split("")
    list_str = str.split(" ")

    if list_s.length != list_str.length
        return false
    end

    for i in 0..list_s.length
        if dict_map.key?(list_s[i])
            if dict_map[list_s[i]] != list_str[i]
                return false
            end
        else
            dict_map[list_s[i]] = list_str[i]
        end
    end

    return true
end


puts areFollowingPatterns(string1, str1)
puts areFollowingPatterns(string2, str2)
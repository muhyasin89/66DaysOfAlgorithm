dict_map = {"{"=> "}", "["=> "]", "("=> ")", "<"=> ">"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  # expected True
inp_str5 = "{{{{{{" #expected False

def ValidateBracket(str, dict_map)
    list_bracket = []
    list_str = str.split("")

    for i in 0..list_str.length()
        temp = list_str[i]
        if dict_map.has_value?(temp) && i< 1
            return false
        elsif  dict_map.key?(temp)
            list_bracket.append(temp)
        elsif dict_map.has_value?(temp)
            if dict_map[list_bracket.last] != temp
                return false
            else
                list_bracket.pop
            end
        end
    end

    if list_bracket.length() > 0
        return false
    end
    return true
end

puts ValidateBracket(inp_str, dict_map)
puts ValidateBracket(inp_str1, dict_map)
puts ValidateBracket(inp_str2, dict_map)
puts ValidateBracket(inp_str3, dict_map)
puts ValidateBracket(inp_str4, dict_map)
puts ValidateBracket(inp_str5, dict_map)
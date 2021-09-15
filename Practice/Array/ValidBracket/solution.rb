dict_map = {"{"=> "}", "["=> "]", "("=> ")", "<"=> ">"}

inp_str = "[]"  # expected True
inp_str1 = "{([{}()[]])}"  # expected True
inp_str2 = "{(][)}"  # expected False
inp_str3 = "]["  # expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  # expected True


def ValidBracket(str, dict_map)
    list_str = str.split("")
    list_bracket = []

    for i in 0..list_str.length()
        if dict_map.has_value?(list_str[i]) && i <1
            return false
        elsif dict_map.key?(list_str[i])
            list_bracket.append(list_str[i])
        elsif dict_map.has_value?(list_str[i])
            if dict_map[list_bracket.last] != list_str[i]
                return false
            else 
                list_bracket.pop
            end
        end 
    end

    return true
end

puts ValidBracket(inp_str, dict_map)
puts ValidBracket(inp_str1, dict_map)
puts ValidBracket(inp_str2, dict_map)
puts ValidBracket(inp_str3, dict_map)
puts ValidBracket(inp_str4, dict_map)
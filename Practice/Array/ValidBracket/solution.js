inp_str = "[]"  // expected True
inp_str1 = "{([{}()[]])}"  // expected True
inp_str2 = "{(][)}"  // expected False
inp_str3 = "]["  // expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  // expected True
inp_str5 = "{{{{{{"  // expected False

dict_map = new Map([
    ["{", "}"],
    ["[", "]"],
    ["(", ")"],
    ["<", ">"]
]);

const ValidateBracket = (str1, dict_map) =>{
    list_bracket = []
    list_str = str1.split("")

    for(let i=0; i< list_str.length; i++){
        temp = list_str[i];

        if(Array.from(dict_map.values()).includes(temp) && i <1){
            return false;
        }else if(dict_map.has(temp)){
            list_bracket.push(temp);
        }else if(Array.from(dict_map.values()).includes(temp)){
            if(list_bracket.length > 0){
                if(dict_map.get(list_bracket[list_bracket.length-1]) !=  temp){
                    return false
                }else{
                    list_bracket.pop();
                }
            }
        }
    }

    if(list_bracket.length >0 ){
        return false;
    }
    return true;
}


console.log(ValidateBracket(inp_str, dict_map));
console.log(ValidateBracket(inp_str1, dict_map));
console.log(ValidateBracket(inp_str2, dict_map));
console.log(ValidateBracket(inp_str3, dict_map));
console.log(ValidateBracket(inp_str4, dict_map));
console.log(ValidateBracket(inp_str5, dict_map));


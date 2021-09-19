inp_str = "[]"  // expected True
inp_str1 = "{([{}()[]])}"  // expected True
inp_str2 = "{(][)}"  // expected False
inp_str3 = "]["  // expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  // expected True

dict_map = new Map([
    ["{", "}"],
    ["[", "]"],
    ["(", ")"],
    ["<", ">"]
]);

const ValidateBracket = (str, dict_map) =>{
    let list_bracket =[];
    let list_str = str.split("");

    if(list_str.length == 1){
        return false
    }

    for(var i=0; i< list_str.length;i++){
        if(Array.from(dict_map.values()).includes(list_str[i]) && i <0){
            return false;
        }else if(dict_map.has(list_str[i])){
            list_bracket.push(list_str[i])
        }else if(Array.from(dict_map.values()).includes(list_str[i])){
            if(dict_map.get(list_bracket[list_bracket.length-1]) !=list_str[i]){
                return false;
            }else{
                list_bracket.pop()
            }
        }
    }
    
    if(list_bracket.length > 0){
        return false;
    }

    return true;
}

console.log(ValidateBracket(inp_str, dict_map));
console.log(ValidateBracket(inp_str1, dict_map));
console.log(ValidateBracket(inp_str2, dict_map));
console.log(ValidateBracket(inp_str3, dict_map));
console.log(ValidateBracket(inp_str4, dict_map));
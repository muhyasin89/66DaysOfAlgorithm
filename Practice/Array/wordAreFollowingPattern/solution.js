
str1  = "abba"
string1 = "dog cat cat dog"
//result True

 
str2 = "abba"
string2= "dog cat cat fish"
//return False


const checkFollowingPattern = (str1, string1) =>{
    hash_map = new Map();
    list_str = str1.split("")
    list_string = string1.split(" ")

    if(list_str.length != list_string.length){
        return false;
    }

    

    for(let i=0; i< list_str.length;i++){
        temp = list_str[i];
        if(hash_map.has(temp)){
            if(hash_map.get(temp)!= list_string[i]){
                return false;
            }
        }else{
            hash_map.set(temp, list_string[i]);
        }
    }

    return true;
}

console.log(checkFollowingPattern(str1,string1))
console.log(checkFollowingPattern(str2,string2))
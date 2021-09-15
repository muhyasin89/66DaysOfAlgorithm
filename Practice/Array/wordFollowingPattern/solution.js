string1 = "abba"
str1 = "dog cat cat dog"
//result True

string2 = "abba"
str2 = "dog cat cat fish"
//return False


const areFollowingPatterns = (s, str) =>{
    m = new Map();
    list_s = s.split("");
    list_str = str.split(" ");

    if(list_s.length != list_str.length){
        return false;
    }

    for(let i=0;i< list_s.length; i++){
        if(m.has(list_s[i])){
            if(m.get(list_s[i]) != list_str[i]){
                return false;
            }
        }else{
            m[list_s[i]] = list_str[i]
        }
    }
    return true;
}

console.log(areFollowingPatterns(str1, string1));
console.log(areFollowingPatterns(str2, string2));
let str1 = "Hello"  // olleH
let str2 = "Test" // tseT
let str3 = "Howdy"  // ydwoH


const reverse = (s) =>{
    return [...s].reverse().join("");
}

console.log(reverse(str1));
console.log(reverse(str2));
console.log(reverse(str3));
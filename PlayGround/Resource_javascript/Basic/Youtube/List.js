let first_string = "Hello World"
let first_int = 11223344

let list_str = first_string.split("");
// Array.from(first_int);
// Object.assign([], first_int);


console.log(list_str);
list_str.splice(5, 1);
console.log(list_str);

console.log(list_int);

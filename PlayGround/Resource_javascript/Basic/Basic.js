


// ES6
// let myName = "Muh Yasin";
// let age = 20;
// const list = [1,2,3,4,5,6]

// console.log(list);
// // for(let i=0; i< list.length; i++){
// //     console.log(i);
// // }

// console.log(`Hello my name is  ${myName} let age ${age}`);

// function getBook(title, author){
//     return {
//         title,
//         author
//     }
// }

// var book = getBook('book apa ini', 'muhyasin');
// console.log(book);


// var user = {
//     name: "muhYasin",
//     age: 25
// }

// console.log(`Hello my name is  ${user.name} let age ${user.name}`);

const shoppingList = {
    name: "Shopping List",
    items:['milk', 'syrup', 'snack', 'egg']
}

// const {name, items} = shoppingList;

// console.log(`hi my name is  ${name} i buy ${items}`);

// var sayAge = function(){
//     console.log("My Age is Secret..")
// }

// console.log(sayAge());

// const sayLocation = (location,name) => {
//     console.log(`My Location is ${location} and my name is ${name}`)
// }

// sayLocation('jakarta', 'muhy yasin');

// old
// var user = {
//     name: "Muh yasin",
//     age : 25,
//     sayName: function(){
//         console.log("My Name is "+ this.name);
//         var that = this;
//         var fullName = function(){
//             console.log("My Name is "+ that.name + " and age is "+ that.age);
//         }
//         fullName();
//     }
// }

const user = {
    name: "Muh Yasin",
    age: 25,
    sayName: function(){
        console.log("My Name is "+ this.name);
        const fullName = () => {
            console.log("My Name is "+ this.name + " and age is "+ this.age);
        }
        fullName();
    }
}

user.sayName();


shoppingList.items.forEach((items, index) => {
    console.log(`index ${index} the item is ${items}`)
});


const newList = shoppingList.items.map(item => item + " new");
console.log(newList);

const filterList = shoppingList.items.filter(item => {
    return item == "milk";
})

console.log(filterList);


function Person(name, age, occupation){
    this.name = name;
    this.age = age;
    this.occupation = occupation;
}

Person.prototype.sayName = function(){
    console.log("My Name is "+this.name);
}

// var yasin = new Person("Muh Yasin", 27, "developer");
// yasin.sayName();

function Profile(avatar, hobbys, name, age, occupation){
    Person.call(this, name, age, occupation);
    this.hobbys = hobbys;
    this.avatar = avatar;
}

Profile.prototype = Object.create(Person.prototype);

const person = Profile('so handsome', 'coding', 'muh yasin', 27, 'developer');
console.log(person);


class ShoppingListClass{
    constructor(items, num){
        this.items = items;
        this.num = num;
    }


    sayList(){
        console.log(this.items);
    }
}

const myList = new ShoppingListClass(['milk', 'apple', 'pear', 'soy milk'], 4);

console.log(myList)

myList.sayList();

class Product extends ShoppingListClass{
    constructor(items, nr, ammount, cost){
        super(items, nr)
        this.ammount = ammount;
        this.cost = cost;
    }
}

const ProductList = new Product(['milk', 'apple', 'pear', 'soy milk'], 4, 2, 40000);

console.log(ProductList);

ProductList.sayList();
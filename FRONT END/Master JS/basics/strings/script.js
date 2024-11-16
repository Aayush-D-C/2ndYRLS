let name="Aayush"
console.log(name.at(2));

//length
let length = name.length;
console.log("Length of String:",length);

//uppercase
console.log(name.toUpperCase())

//lowercase
console.log(name.toLowerCase())

//Substring to extract a portion of string
console.log(name.substring(0,4))

//String search 
let i = name.indexOf('a');
console.log("The letter 'a' is found in index:",i);

//String Replace
let s1 = "He is great";

let s2 = s1.replace("He","She");

console.log(s2);


//Trimming whitespace from String

let a1 = "           Aayush Dangi             "
console.log(a1);

//Chaining of methods
console.log(a1.trim().toUpperCase());

//String Comparison

let h1 = "Aayush"

let h2 = "Prasis"

if(h1==h2){
    console.log("String match");
}

else{
    console.log("String no match");
}

/*
    Are the strings created by the new keyword is same as normal strings?

    No, the string created by the new keyword is an object and is not the same as normal strings.
*/

const str1 = new String("GeeksforGeeks");
const str2 = "GeeksforGeeks";
console.log(typeof(str1)+"\n"+typeof(str2))
console.log(str1 == str2);
console.log(str1 === str2);
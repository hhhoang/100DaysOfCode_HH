/*
We have an array of objects representing different people in our contacts lists.
A lookUpProfile function that takes name and a property (prop) as arguments has been pre-written for you.
The function should check if name is an actual contact's firstName and the given property (prop) is a property of that contact.
*/



//Setup
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
];


function lookUpProfile(name, prop){
// Only change code below this line
  for (var i = 0; i < contacts.length; i++){
      if (contacts[i]["firstName"] === name){
        if (contacts[i].hasOwnProperty(prop)){
            return contacts[i][prop];
        } else {
            console.log("No such property");
            return "No such property";
        }
      } 
  }
  return "No such contact";
// Only change code above this line
}

// Change these values to test your function
lookUpProfile("Kristian", "lastName");

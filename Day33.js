// https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/record-collection
/* You are given a JSON object representing a part of your musical album collection. 
Each album has several properties and a unique id number as its key. Not all albums have complete information.
Write a function which takes an album's id (like 2548), a property prop (like "artist" or "tracks"), 
and a value (like "Addicted to Love") to modify the data in this collection. */

// Setup
var collection = {
    "2548": {
      "album": "Slippery When Wet",
      "artist": "Bon Jovi",
      "tracks": [ 
        "Let It Rock", 
        "You Give Love a Bad Name" 
      ]
    },
    "2468": {
      "album": "1999",
      "artist": "Prince",
      "tracks": [ 
        "1999", 
        "Little Red Corvette" 
      ]
    },
    "1245": {
      "artist": "Robert Palmer",
      "tracks": [ ]
    },
    "5439": {
      "album": "ABBA Gold"
    }
};
// Keep a copy of the collection for tests
var collectionCopy = JSON.parse(JSON.stringify(collection));

// Only change code below this line
function updateRecords(id, prop, value) {
  var prop_object = collection[id];
  if (prop !== "tracks"){
    prop_object[prop] = value;
  } else{
    console.log(prop_object[prop])
    if (prop_object[prop] == undefined){
      prop_object[prop] = [];
      prop_object[prop].push(value);
    } else{
      prop_object[prop].push(value);
    }
  }
  if (value == ""){
    delete prop_object[prop];
  } 
  return collection;
}

// Alter values below to test your code
//updateRecords(5439, "artist", "ABBA");

#!/usr/bin/node

// Import array and compute a new array
const mylist = require('./100-data.js').list;
const newList = mylist.map(x => x * mylist.indexOf(x));

console.log(mylist);
console.log(newList);

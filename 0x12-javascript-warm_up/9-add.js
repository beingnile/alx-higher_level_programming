#!/usr/bin/node

// Define function for addition

function add (a, b) {
  return a + b;
}

// Parse arguments and print the result after addition

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));

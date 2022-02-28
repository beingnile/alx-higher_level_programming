#!/usr/bin/node

// Define factorial function recursively

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  }

  return (num * factorial(num - 1));
}

// Parse argument

const arg = parseInt(process.argv[2]);

// Print out result of factorial

console.log(factorial(arg));

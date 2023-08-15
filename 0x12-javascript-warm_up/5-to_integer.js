#!/usr/bin/node
const args = process.argv;
const result = parseInt(args[2]);

if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${result}`);
}

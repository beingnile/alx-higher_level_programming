#!/usr/bin/node
const args = process.argv;
const occurences = parseInt(args[2]);

if (isNaN(occurences)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
}

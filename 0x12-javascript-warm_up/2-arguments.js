#!/usr/bin/node

// import { argv } from 'process';
// Check if the length of argv is greater than 2

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

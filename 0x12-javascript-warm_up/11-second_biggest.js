#!/usr/bin/node

// Search for the second biggest element in arguments
// and print it out

if (process.argv.length <= 3) {
  console.log('0');
} else {
  // Slice the arguments
  const arr = process.argv.slice(2);

  // Sort the sliced arguments
  arr.sort((a, b) => b - a);

  // Print out the second largest
  console.log(arr[1]);
}

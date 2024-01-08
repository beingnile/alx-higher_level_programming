#!/usr/bin/node
let arr = process.argv;

for (const item of arr) {
  arr[arr.indexOf(item)] = parseInt(item);
}

arr = arr.slice(2);

if (arr.length <= 3) {
  console.log(0);
} else {
  console.log(arr.sort().pop());
}

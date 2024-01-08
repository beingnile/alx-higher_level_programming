#!/usr/bin/node
const raw = process.argv.slice(2);
const arr = [];

for (const item of raw) {
  arr.push(parseInt(item));
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(arr.sort().slice(-2)[0]);
}

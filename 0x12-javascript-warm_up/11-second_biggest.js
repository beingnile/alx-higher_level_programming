#!/usr/bin/node
const raw = process.argv.slice(2);
const arr = raw.map((x) => parseInt(x));

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(arr.sort((a, b) => a - b).slice(-2)[0]);
}

#!/usr/bin/node
const num = Number(process.argv[2]);

function factorial (a) {
  let result = 0;
  if (isNaN(a)) {
    return (1);
  }

  if (a === 1) {
    return (1);
  }

  result = a * factorial(a - 1);

  return (result);
}

console.log(factorial(num));

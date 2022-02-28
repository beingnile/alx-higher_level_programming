#!/usr/bin/node

// Print square
// Take first argument as the size of the square
// Use nested loop to print square

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let width = 0; width < size; width++) {
    let line = '';
    for (let height = 0; height < size; height++) {
      line += 'X';
    }
    console.log(line);
  }
}

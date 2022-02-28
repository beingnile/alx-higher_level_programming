#!/usr/bin/node

// Set variable for parsed int

let count = parseInt(process.argv[2]);

// Check if argument is NaN
// If it is, print message, else, print C is fun count times

if isNaN(count) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < count; count++) {
		console.log('C is fun');
	}
}

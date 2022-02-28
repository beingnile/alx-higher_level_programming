#!/usr/bin/node

let num = parseInt(process.argv[2]);
if (num === 'NaN') {
	console.log('Not a number');
} else {
	console.log(num);
}

#!/usr/bin/node

const mydict = require('./101-data.js').dict;
const newdict = Object.assign({}, ...Object.entries(mydict).map(([a, b]) => ({ [b]: [a] })));

console.log(newdict);

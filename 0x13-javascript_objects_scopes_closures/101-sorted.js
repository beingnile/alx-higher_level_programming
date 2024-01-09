#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = Object.entries(dict).reduce((acc, [userId, occurrences]) => {
  if (!acc[occurrences]) {
    acc[occurrences] = [];
  }
  acc[occurrences].push(userId);
  return acc;
}, {});

console.log(sortedDict);
